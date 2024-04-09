from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QPixmap, QImage
import leap
import time
from timeit import default_timer as timer
from typing import Callable
from datetime import datetime
import pandas as pd
import numpy as np
import cv2


# This function converts an OpenCV image to QImage format
def cv2_to_qimage(cv_img):
    height, width, channel = cv_img.shape
    bytes_per_line = 3 * width
    qimage = QImage(
        cv_img.data, width, height, bytes_per_line, QImage.Format.Format_RGB888
    ).rgbSwapped()

    return qimage


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
    imageUpdated = Signal(dict)

    def __init__(self):
        leap.Listener.__init__(self)
        QObject.__init__(self)  # Initialize QObject
        self.device_latest_tracking_event = {}
        self.device_mappings = {}
        self.bone_coordinates = {}
        self.finger_names = ["thumb", "index", "middle", "ring", "pinky"]
        self.bone_names = ["metacarpal", "proximal", "intermediate", "distal"]

        # Device Connection Initializations
        self.device_connection_status = {"top": False, "bottom": False, "side": False}
        self.top_device_id = "LP85571778017"
        self.bottom_device_id = "LP76907386047"
        self.side_device_id = "LP19298121554"

        # Recording Initializations
        self.start_time = None
        self.collecting_data = False
        self.device_counter = 1

        # File Information Initializations
        self.filename_info = {"name": "default", "id": "default", "date": "default"}
        self.is_recording_tracking = False

        # Real-time UI Data Initializations
        self.real_time_ui_data = {}

        # Real Time Skeleton Data Initializations
        self.screen_size = [500, 700]
        self.hands_colour = (255, 255, 255)
        self.font_colour = (0, 255, 44)
        self.hands_format = "Skeleton"
        self.output_images = {}
        self.tracking_mode = None

        # Frequency of sending real-time data
        self.last_sample_time = time.time()
        self.sampling_rate_hz = 42
        self.desired_interval = 1.0 / self.sampling_rate_hz

    def number_of_devices_tracking(self):
        return len(self.device_latest_tracking_event)

    ############################################################################################################
    # Device Status Sending Signal
    ############################################################################################################

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

    ############################################################################################################
    # Skeleton Rendering Sending Signal
    ############################################################################################################

    def set_tracking_mode(self, tracking_mode):
        self.tracking_mode = tracking_mode

    def toggle_hands_format(self):
        self.hands_format = "Skeleton"
        print(f"Set hands format to {self.hands_format}")

    def get_joint_position(self, bone):
        if bone:
            return int(bone.x + (self.screen_size[1] / 2)), int(
                bone.z + (self.screen_size[0] / 2)
            )
        else:
            return None

    def render_hands(self, event):
        print("Entered render_hands")  # Debug print
        device_id = event.metadata.device_id
        print(f"Rendering hands for device_id: {device_id}")

        # Correctly initialize an entry for device_id if it doesn't exist
        if device_id not in self.output_images:
            self.output_images[device_id] = np.zeros(
                (self.screen_size[0], self.screen_size[1], 3), np.uint8
            )

        # Now it's safe to access output_image, since we've ensured its initialization
        output_image = self.output_images[device_id]
        output_image.fill(0)  # Clear the image

        if len(event.hands) == 0:
            return

        for i in range(0, len(event.hands)):
            hand = event.hands[i]
            for index_digit in range(0, 5):
                digit = hand.digits[index_digit]
                for index_bone in range(0, 4):
                    bone = digit.bones[index_bone]
                    wrist = self.get_joint_position(hand.arm.next_joint)
                    elbow = self.get_joint_position(hand.arm.prev_joint)
                    if wrist:
                        cv2.circle(output_image, wrist, 3, self.hands_colour, -1)
                    if elbow:
                        cv2.circle(output_image, elbow, 3, self.hands_colour, -1)
                    if wrist and elbow:
                        cv2.line(output_image, wrist, elbow, self.hands_colour, 2)

                    bone_start = self.get_joint_position(bone.prev_joint)
                    bone_end = self.get_joint_position(bone.next_joint)
                    if bone_start:
                        cv2.circle(output_image, bone_start, 3, self.hands_colour, -1)
                    if bone_end:
                        cv2.circle(output_image, bone_end, 3, self.hands_colour, -1)
                    if bone_start and bone_end:
                        cv2.line(
                            output_image,
                            bone_start,
                            bone_end,
                            self.hands_colour,
                            2,
                        )

                    # Connecting digits logic
                    if ((index_digit == 0) and (index_bone == 0)) or (
                        (index_digit > 0) and (index_digit < 4) and (index_bone < 2)
                    ):
                        index_digit_next = index_digit + 1
                        digit_next = hand.digits[index_digit_next]
                        bone_next = digit_next.bones[index_bone]
                        bone_next_start = self.get_joint_position(bone_next.prev_joint)
                        if bone_start and bone_next_start:
                            cv2.line(
                                output_image,
                                bone_start,
                                bone_next_start,
                                self.hands_colour,
                                2,
                            )
                    if index_bone == 0 and bone_start and wrist:
                        cv2.line(output_image, bone_start, wrist, self.hands_colour, 2)

    def emit_images_for_all_devices(self):
        for device_id, image in self.output_images.items():
            qimage = cv2_to_qimage(image)
            if not qimage.isNull():
                print(f"Emitting imageUpdated signal for device_id: {device_id}")
                self.imageUpdated.emit({"device_id": device_id, "image": qimage})
            else:
                print(f"Failed to create a valid QImage for device_id: {device_id}")

    # Event handling methods
    def on_tracking_mode_event(self, event):
        self.set_tracking_mode(event.current_tracking_mode)

    ############################################################################################################
    # Real Time Data Sending Signal
    ############################################################################################################

    @Slot(bool)
    def toggle_recording_slot(self, is_recording_tracking):
        # print(f"Before toggle, recording status: {self.is_recording_tracking}")
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
        # print(f"After toggle, recording status: {self.is_recording_tracking}")

    def on_tracking_event(self, event):
        print(
            f"Debug: on_tracking_event called with recording status = {self.is_recording_tracking}"
        )

        # Check if recording should be active
        if not self.is_recording_tracking:
            return

        current_time = time.time()

        # Detect hand and start collecting data after 3 seconds
        if not self.start_time and len(event.hands) > 0:
            print("Hand detected. Will start collecting data...")
            self.start_time = current_time

        # Start collecting data after 3 seconds
        if self.start_time and not self.collecting_data:
            elapsed_time = current_time - self.start_time
            if elapsed_time >= 3:
                self.collecting_data = True
                print("Start rendering hands")

        # Collect data based on the desired time interval (for 42Hz, interval is ~0.0238 seconds)
        desired_interval = 1 / 42.0  # Approximate interval for 42Hz
        if (
            self.collecting_data
            and (current_time - self.last_sample_time) >= desired_interval
        ):
            self.last_sample_time = current_time  # Update the last sample time

            self.render_hands(event)
            self.emit_images_for_all_devices()

            # Sample data collection logic
            device_id = event.metadata.device_id
            device_identifier = self.device_mappings.get(
                device_id, f"device_{self.device_counter}"
            )
            if device_id not in self.device_mappings:
                self.device_mappings[device_id] = device_identifier
                self.device_counter += 1

            timestamp = datetime.now().strftime("%H:%M:%S")
            self.collect_and_emit_data(event, timestamp, device_identifier)

    def collect_and_emit_data(self, event, timestamp, device_identifier):
        for hand in event.hands:
            for index_digit, digit in enumerate(hand.digits):
                finger_name = self.finger_names[index_digit]
                for index_bone, bone in enumerate(digit.bones):
                    bone_name = self.bone_names[index_bone]
                    key = (timestamp, bone_name)
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

                    # Prepare data for real-time UI update and emit signal
                    data = {
                        "finger_name": finger_name,
                        "bone_name": bone_name,
                        "device_id": device_identifier,
                        "start_x": f"{bone.prev_joint.x:.2f}",
                    }
                    self.realTimeDataUpdated.emit(data)

    ############################################################################################################
    # File Information Receive Slot
    ############################################################################################################

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
                wait_until(lambda: self.device_listener.n_events == 3, timeout=1000)
                get_updated_devices(connection)

                # Initial check before entering the loop
                while self._isRunning:
                    time.sleep(0.5)
        finally:
            self.finished.emit()

    def requestStop(self):
        self._isRunning = False
