import leap
import time
from timeit import default_timer as timer
from typing import Callable
from PySide6.QtCore import QObject, Signal, Slot, QTimer
from datetime import datetime
import pandas as pd


class MultiDeviceListener(leap.Listener):
    def __init__(self, event_type):
        super().__init__()
        self._event_type = event_type
        self.n_events = 0

    def on_event(self, event):
        if isinstance(event, self._event_type):
            self.n_events += 1


def wait_until(
    condition: Callable[[], bool], timeout: float = 5, poll_delay: float = 0.01
):
    start_time = timer()
    while timer() - start_time < timeout:
        if condition():
            return True
        time.sleep(poll_delay)
    return False  # Time expired


class TrackingEventListener(leap.Listener, QObject):
    deviceStatusChanged = Signal(str, bool)
    realTimeDataUpdated = Signal(dict)

    def __init__(self):
        leap.Listener.__init__(self)
        QObject.__init__(self)  # Initialize QObject
        self.device_latest_tracking_event = {}
        self.device_mappings = {}
        self.bone_coordinates = {}
        self.finger_names = ["thumb", "index", "middle", "ring", "pinky"]
        self.bone_names = ["metacarpal", "proximal", "intermediate", "distal"]
        self.device_connection_status = {"top": False, "bottom": False, "side": False}
        self.top_device_id = "LP85571778017"
        self.bottom_device_id = "LP76907386047"
        self.side_device_id = "LP19298121554"
        self.start_time = None
        self.collecting_data = False
        self.device_counter = 1
        self.filename_info = {"name": "default", "id": "default", "date": "default"}
        self.is_recording_tracking = False
        self.real_time_ui_data = {}

    def number_of_devices_tracking(self):
        return len(self.device_latest_tracking_event)

    def on_device_event(self, event):
        with event.device.open():
            info = event.device.get_info()

        print(f"Emitting deviceStatusChanged signal for {info.serial}")

        self.deviceStatusChanged.emit(
            info.serial,
            (
                True
                if info.serial
                in [self.top_device_id, self.bottom_device_id, self.side_device_id]
                else False
            ),
        )

    @Slot(bool)
    def toggle_recording_slot(self, is_recording_tracking):
        print(f"Before toggle, recording status: {self.is_recording_tracking}")
        if self.is_recording_tracking and not is_recording_tracking:
            # If we're stopping the recording, save the data
            self.save_coordinates_to_csv(self.bone_coordinates)
            # Resetting the variables after saving data for the next session.
            self.start_time = None
            self.collecting_data = False
            self.bone_coordinates = (
                {}
            )  # Optionally reset bone coordinates if you want to start fresh
        elif not self.is_recording_tracking and is_recording_tracking:
            # If we're about to start recording, ensure states are reset
            self.start_time = None
            self.collecting_data = False
        self.is_recording_tracking = is_recording_tracking
        print(f"After toggle, recording status: {self.is_recording_tracking}")

    def on_tracking_event(self, event):
        print(
            f"Debug: on_tracking_event called BEFORE is_recording_tracking toggled = {self.is_recording_tracking}"
        )
        # 0. Check if recording should be active
        if self.is_recording_tracking == False:
            return
        print(
            f"Debug: on_tracking_event called AFTER is_recording_tracking toggled = {self.is_recording_tracking}"
        )

        # 1. Detect hand and start collecting data after 3 seconds
        if not self.start_time and len(event.hands) > 0:
            print("Hand detected. Will start collecting data...")
            self.start_time = timer()

        # 2. Start collecting data after 3 seconds
        if self.start_time and not self.collecting_data:
            elapsed_time = timer() - self.start_time
            if elapsed_time >= 3:
                self.collecting_data = True
                for i in range(3, 0, -1):
                    print(f"Start in {i}")
                    time.sleep(1)
                print("start")

        # 3. Collect data every 2 frames
        if self.collecting_data and event.tracking_frame_id % 2 == 0:
            device_id = event.metadata.device_id

            if device_id not in self.device_mappings:
                self.device_mappings[device_id] = f"device_{self.device_counter}"
                self.device_counter += 1

            device_identifier = self.device_mappings[device_id]

            timestamp = datetime.now().strftime("%H:%M:%S")

            for hand in event.hands:
                for index_digit, digit in enumerate(hand.digits):
                    finger_name = self.finger_names[index_digit]
                    for index_bone, bone in enumerate(digit.bones):
                        bone_name = self.bone_names[index_bone]
                        key = (
                            timestamp,
                            bone_name,
                        )
                        if key not in self.bone_coordinates:
                            self.bone_coordinates[key] = {
                                "timestamp": timestamp,
                                "bone_index": bone_name,
                            }
                        self.bone_coordinates[key].update(
                            {
                                f"{finger_name}_start_x_{device_identifier}": bone.prev_joint.x,
                                f"{finger_name}_start_y_{device_identifier}": bone.prev_joint.y,
                                f"{finger_name}_start_z_{device_identifier}": bone.prev_joint.z,
                                f"{finger_name}_end_x_{device_identifier}": bone.next_joint.x,
                                f"{finger_name}_end_y_{device_identifier}": bone.next_joint.y,
                                f"{finger_name}_end_z_{device_identifier}": bone.next_joint.z,
                            }
                        )

                        # print(
                        #     f"Device: {device_id}   Bone {self.bone_names[index_bone]} of Digit {self.finger_names[index_digit]} Prev Joint Position: {bone.prev_joint.x, bone.prev_joint.y, bone.prev_joint.z}, Next Joint Position: {bone.next_joint.x, bone.next_joint.y, bone.next_joint.z}"
                        # )

                        # Populate real_time_ui_data for UI updates and format start_x
                        if device_identifier not in self.real_time_ui_data:
                            self.real_time_ui_data[device_identifier] = {}
                        if finger_name not in self.real_time_ui_data[device_identifier]:
                            self.real_time_ui_data[device_identifier][finger_name] = {}
                        self.real_time_ui_data[device_identifier][finger_name][
                            bone_name
                        ] = f"{bone.prev_joint.x:.2f}"

                        data = {
                            "finger_name": finger_name,
                            "bone_name": bone_name,
                            "device_id": device_identifier,
                            "start_x": f"{bone.prev_joint.x:.2f}",
                        }
                        self.realTimeDataUpdated.emit(data)

    def set_filename_info_slot(self, name, id, date):
        self.filename_info["name"] = name
        self.filename_info["id"] = id
        self.filename_info["date"] = date

    def save_coordinates_to_csv(self, bone_coordinates):
        if not self.bone_coordinates:
            print("No data to save.")
            return

        # Generate the filename using the stored user information
        filename = f"{self.filename_info['name']}_{self.filename_info['id']}_{self.filename_info['date']}.csv"

        records = [value for key, value in self.bone_coordinates.items()]
        df = pd.DataFrame(records)
        df.to_csv(filename, index=False)
        print(f"Coordinates saved to CSV: {filename}")


def get_updated_devices(connection):
    devices = connection.get_devices()
    for device in devices:
        with device.open():
            connection.subscribe_events(device)


class LeapMotionWorker(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()
        self._isRunning = True
        self.tracking_listener = TrackingEventListener()

    def run(self):
        self.device_listener = MultiDeviceListener(leap.events.DeviceEvent)

        connection = leap.Connection(multi_device_aware=True)
        connection.add_listener(self.tracking_listener)
        connection.add_listener(self.device_listener)

        try:
            with connection.open():
                wait_until(lambda: self.device_listener.n_events > 0)
                get_updated_devices(connection)

                # Initial check before entering the loop
                while self._isRunning:
                    time.sleep(0.5)
        finally:
            self.finished.emit()

    def requestStop(self):
        self._isRunning = False
