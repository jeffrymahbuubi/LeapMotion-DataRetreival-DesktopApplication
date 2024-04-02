import leap
import time
from timeit import default_timer as timer

from leap.events import Event


class TrackingEventListener(leap.Listener):
    def __init__(self):
        super().__init__()
        self.device_latest_tracking_event = {}
        self.device_mappings = {}
        self.bone_coordinates = {}
        self.finger_names = ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        self.bone_names = ["Metacarpal", "Proximal", "Intermediate", "Distal"]
        self.start_time = None
        self.collecting_data = False
        self.device_counter = 1

    def on_tracking_event(self, event):
        if not self.start_time and len(event.hands) > 0:
            print("Hand detected. Will start collecting data...")
            self.start_time = timer()

        if self.start_time and not self.collecting_data:
            elapsed_time = timer() - self.start_time
            if elapsed_time >= 3:
                self.collecting_data = True
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
                print("start")

        if self.collecting_data and event.tracking_frame_id % 2 == 0:
            device_id = event.metadata.device_id
            print(f"Device ID: {device_id}")


def main():
    tracking_listener = TrackingEventListener()
    connection = leap.Connection()
    connection.add_listener(tracking_listener)

    running = True

    with connection.open():
        connection.set_tracking_mode(leap.TrackingMode.Desktop)
        while running:
            time.sleep(1)


if __name__ == "__main__":
    main()
