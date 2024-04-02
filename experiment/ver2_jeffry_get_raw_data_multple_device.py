"""Prints tracking events from multiple devices. We create a listener to get
device events to get an updated device list from the connection. The tracking
listener is much the same as the `tracking_event_example.py` but the serial
number of each tracking event is logged too. The tracking events are only
logged every 100 frames.
"""

import leap
import time
from timeit import default_timer as timer
from typing import Callable
from leap.events import TrackingEvent
from leap.event_listener import LatestEventListener
from leap.datatypes import FrameData
from datetime import datetime, timedelta
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
    if not condition():
        return False


class TrackingEventListener(leap.Listener):
    def __init__(self):
        super().__init__()
        self.device_latest_tracking_event = {}
        self.device_mappings = {}
        self.bone_coordinates = {}
        self.finger_names = ["thumb", "index", "middle", "ring", "pinky"]
        self.bone_names = ["metacarpal", "proximal", "intermediate", "distal"]
        self.top_device_id = "LP85571778017"
        self.bottom_device_id = "LP76907386047"
        self.side_device_id = "LP19298121554"
        self.start_time = None
        self.collecting_data = False
        self.device_counter = 1

    def on_device_event(self, event):
        try:
            with event.device.open():
                info = event.device.get_info()
        except leap.LeapCannotOpenDeviceError:
            info = event.device.get_info()

        print(f"Info: {info}")
        if info.serial == self.top_device_id:
            print(f"Found top device {info.serial}")
        elif info.serial == self.bottom_device_id:
            print(f"Found bottom device {info.serial}")
        elif info.serial == self.side_device_id:
            print(f"Found side device {info.serial}")

    def on_tracking_event(self, event):
        # 1. Detect hand and start collecting data after 3 seconds
        if self.start_time is None and len(event.hands) > 0:
            print("Hand detected. Will start collecting data...")
            self.start_time = timer()

        # 2. Start collecting data after 3 seconds
        if self.start_time is not None and self.collecting_data is False:
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
            # print(f"Device ID: {device_id}, Device Identifier: {device_identifier}")

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
                        print(
                            f"Bone {self.bone_names[index_bone]} of Digit {self.finger_names[index_digit]} Prev Joint Position: {bone.prev_joint.x, bone.prev_joint.y, bone.prev_joint.z}, Next Joint Position: {bone.next_joint.x, bone.next_joint.y, bone.next_joint.z}"
                        )


def get_updated_devices(connection):
    devices = connection.get_devices()

    for device in devices:
        with device.open():
            connection.subscribe_events(device)


def save_coordinates_to_csv(
    coordinates, filename="bone_coordinates_multiple_device.csv"
):
    if not coordinates:
        print("No data to save.")
        return

    records = [value for key, value in coordinates.items()]
    df = pd.DataFrame(records)
    df.to_csv(filename, index=False)
    print(f"Coordinates saved to CSV: {filename}")


def main():
    tracking_listener = TrackingEventListener()
    device_listener = MultiDeviceListener(leap.events.DeviceEvent)

    connection = leap.Connection(multi_device_aware=True)
    connection.add_listener(tracking_listener)
    connection.add_listener(device_listener)

    try:
        with connection.open():
            wait_until(lambda: device_listener.n_events > 1)
            get_updated_devices(connection)

            while True:
                time.sleep(0.5)  # Reduce CPU usage

    except KeyboardInterrupt:
        print("Stopping and saving data to CSV...")
        save_coordinates_to_csv(tracking_listener.bone_coordinates)
        print("Data saved. Exiting program.")


if __name__ == "__main__":
    main()
