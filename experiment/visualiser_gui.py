import leap
import numpy as np
import cv2
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QThread, pyqtSignal
import sys


_TRACKING_MODES = {leap.TrackingMode.Desktop: "Desktop"}


# This function converts an OpenCV image to QImage format
def cv2_to_qimage(cv_img):
    height, width, channel = cv_img.shape
    bytes_per_line = 3 * width
    qimage = QImage(
        cv_img.data, width, height, bytes_per_line, QImage.Format.Format_RGB888
    ).rgbSwapped()

    return qimage


class TrackingEventListener(leap.Listener):
    def __init__(self):
        super().__init__()
        self.name = "Python Gemini Visualiser"
        self.screen_size = [500, 700]
        self.hands_colour = (255, 255, 255)
        self.font_colour = (0, 255, 44)
        self.hands_format = "Skeleton"
        self.output_image = np.zeros(
            (self.screen_size[0], self.screen_size[1], 3), np.uint8
        )
        self.tracking_mode = None

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
        self.output_image[:, :] = 0  # Clear the previous image
        cv2.putText(
            self.output_image,
            f"Tracking Mode: {_TRACKING_MODES[self.tracking_mode]}",
            (10, self.screen_size[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            self.font_colour,
            1,
        )

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
                        cv2.circle(self.output_image, wrist, 3, self.hands_colour, -1)
                    if elbow:
                        cv2.circle(self.output_image, elbow, 3, self.hands_colour, -1)
                    if wrist and elbow:
                        cv2.line(self.output_image, wrist, elbow, self.hands_colour, 2)

                    bone_start = self.get_joint_position(bone.prev_joint)
                    bone_end = self.get_joint_position(bone.next_joint)
                    if bone_start:
                        cv2.circle(
                            self.output_image, bone_start, 3, self.hands_colour, -1
                        )
                    if bone_end:
                        cv2.circle(
                            self.output_image, bone_end, 3, self.hands_colour, -1
                        )
                    if bone_start and bone_end:
                        cv2.line(
                            self.output_image,
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
                                self.output_image,
                                bone_start,
                                bone_next_start,
                                self.hands_colour,
                                2,
                            )
                    if index_bone == 0 and bone_start and wrist:
                        cv2.line(
                            self.output_image, bone_start, wrist, self.hands_colour, 2
                        )

    # Event handling methods
    def on_tracking_mode_event(self, event):
        self.set_tracking_mode(event.current_tracking_mode)

    def on_tracking_event(self, event):
        self.render_hands(event)


class LeapMotionWorker(QThread):
    image_updated = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()
        self._isRunning = True
        self.tracking_listener = TrackingEventListener()

    def run(self):
        connection = leap.Connection()
        connection.add_listener(self.tracking_listener)

        try:
            with connection.open():
                while self._isRunning:
                    qimage = cv2_to_qimage(self.tracking_listener.output_image)
                    self.image_updated.emit(qimage)
                    self.msleep(1)  # Adjust based on desired refresh rate
        finally:
            self._isRunning = False

    def stop(self):
        self._isRunning = False


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Leap Motion Tracker")
        self.image_label = QLabel(self)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.image_label)
        self.setLayout(self.layout)

    def update_image(self, qimage: QImage):
        pixmap = QPixmap.fromImage(qimage)
        self.image_label.setPixmap(pixmap)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    leap_worker = LeapMotionWorker()
    leap_worker.image_updated.connect(window.update_image)
    leap_worker.start()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
