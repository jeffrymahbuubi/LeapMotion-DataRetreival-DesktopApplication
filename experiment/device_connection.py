import leap
import time
from timeit import default_timer as timer
from typing import Callable


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
        self.top_device_id = "LP85571778017"
        self.bottom_device_id = "LP76907386047"
        self.side_device_id = "LP19298121554"
        self.start_time = None
        self.collecting_data = False
        self.device_counter = 1

    def number_of_devices_tracking(self):
        return len(self.device_latest_tracking_event)

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
        # 1. Detect hand and start collecting data after 3 seconds`
        if not self.start_time and len(event.hands) > 0:
            print("Hand detected. Will start collecting data...")
            self.start_time = timer()

        # 2. Start collecting data after 3 seconds
        if self.start_time and not self.collecting_data:
            elapsed_time = timer() - self.start_time
            if elapsed_time >= 3:
                self.collecting_data = True
                for i in range(3, 0, -1):
                    print(i)
                    time.sleep(1)
                print("start")

        # 3. Collect data every
        if self.collecting_data and event.tracking_frame_id % 2 == 0:
            metadata = event.metadata
            print(f"Metadata: {metadata}")
            device_id = event.metadata.device_id
            print(f"Metadata Device ID:{ device_id}")
            info = event.info
            print(f"Info: {info}")

            # if device_id not in self.device_mappings:
            #     self.device_mappings[device_id] = f"device_{self.device_counter}"
            #     self.device_counter += 1

            # device_identifier = self.device_mappings[device_id]
            # print(f"Device ID: {device_id}, Device Identifier: {device_identifier}")

        self.device_latest_tracking_event[event.metadata.device_id] = event


def get_updated_devices(connection):
    devices = connection.get_devices()

    for device in devices:
        with device.open():
            connection.subscribe_events(device)


def main():
    tracking_listener = TrackingEventListener()
    device_listener = MultiDeviceListener(leap.events.DeviceEvent)

    connection = leap.Connection(multi_device_aware=True)
    connection.add_listener(tracking_listener)
    connection.add_listener(device_listener)

    with connection.open():
        wait_until(lambda: device_listener.n_events > 1)

        current_device_events = device_listener.n_events
        get_updated_devices(connection)

        while True:
            if device_listener.n_events != current_device_events:
                current_device_events = device_listener.n_events
                get_updated_devices(connection)

            time.sleep(0.5)


if __name__ == "__main__":
    main()
