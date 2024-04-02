"""Prints tracking events from multiple devices. We create a listener to get
device events to get an updated device list from the connection. The tracking
listener is much the same as the `tracking_event_example.py` but the serial
number of each tracking event is logged too. The tracking events are only
logged every 100 frames.
"""

import csv

import leap
import time
from timeit import default_timer as timer
from typing import Callable
from leap.events import TrackingEvent
from leap.event_listener import LatestEventListener
from leap.datatypes import FrameData
from datetime import datetime, timedelta


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
        self.device_latest_tracking_event = {}
        self.bone_coordinates = []  # List to store bone coordinates
        self.finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        self.bone_names = ["Metacarpal", "Proximal", "Intermediate", "Distal"]
        self.start_time = None
        self.collecting_data = False

    def number_of_devices_tracking(self):
        return len(self.device_latest_tracking_event)

    def on_tracking_event(self, event):
        # 1. Detect hand and start collecting data after 3 seconds
        if not self.start_time and len(event.hands) > 0:
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

            for i in range(0, len(event.hands)):
                hand = event.hands[i]
                # hand_type = "left" if str(hand.type) == "HandType.Left" else "right"
                # print(
                #     f"Hand id {hand.id} is a {hand_type} hand with position ({hand.palm.position.x}, {hand.palm.position.y}, {hand.palm.position.z})."
                # )
                for index_digit in range(0, 5):
                    digit = hand.digits[index_digit]
                    for index_bone in range(0, 4):
                        bone = digit.bones[index_bone]

                        self.bone_coordinates.append(
                            {
                                "device_id": event.metadata.device_id,
                                "timestamp": datetime.now().strftime("%H:%M:%S"),
                                "frame_id": event.tracking_frame_id,
                                "hand_id": hand.id,
                                # "hand_type": hand_type,
                                "digit_index": self.finger_names[index_digit],
                                "bone_index": self.bone_names[index_bone],
                                "start_x": bone.prev_joint.x,
                                "start_y": bone.prev_joint.y,
                                "start_z": bone.prev_joint.z,
                                "end_x": bone.next_joint.x,
                                "end_y": bone.next_joint.y,
                                "end_z": bone.next_joint.z,
                            }
                        )
                        print(
                            f"Bone {self.bone_names[index_bone]} of Digit {self.finger_names[index_digit]} Prev Joint Position: {bone.prev_joint.x, bone.prev_joint.y, bone.prev_joint.z}, Next Joint Position: {bone.next_joint.x, bone.next_joint.y, bone.next_joint.z}"
                        )

        source_device = event.metadata.device_id
        self.device_latest_tracking_event[source_device] = event


def get_updated_devices(connection):
    devices = connection.get_devices()

    for device in devices:
        with device.open():
            connection.subscribe_events(device)


def save_coordinates_to_csv(
    coordinates, filename="bone_coordinates_multiple_device.csv"
):
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "device_id",
                "timestamp",
                "frame_id",
                "hand_id",
                # "hand_type",
                "digit_index",
                "bone_index",
                "start_x",
                "start_y",
                "start_z",
                "end_x",
                "end_y",
                "end_z",
            ],
        )
        writer.writeheader()
        for coord in coordinates:
            writer.writerow(coord)
    print("Coordinates saved to CSV.")


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
