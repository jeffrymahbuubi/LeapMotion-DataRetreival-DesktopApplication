from PySide6.QtWidgets import QMainWindow, QApplication
import sys
from PySide6.QtGui import QIcon
from leapmotion_ver3 import Ui_MainWindow
from data_management_ui import DataManagementUI
from leapmotion_logic import TrackingEventListener, LeapMotionWorker
from PySide6.QtCore import QThread, Qt


class Application(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Leap Motion Gemini V1.0")
        self.setWindowIcon(QIcon("images/WTMH.ico"))
        self.tracking_listener = TrackingEventListener()

        # Assuming you have a method or properties to initialize labels and buttons
        self.data_management_ui = DataManagementUI(
            self.device_top_status,
            self.device_bottom_status,
            self.device_side_status,
            self.recordButton,
            self.name_for_csv,
            self.id_for_csv,
            self.date_for_csv,
            self.metacarpal_table,
            self.proximal_table,
            self.intermediate_table,
            self.distal_table,
        )

        # Start Leap Motion in a separate thread
        self.start_leap_motion_thread()

    def start_leap_motion_thread(self):
        self.thread = QThread()
        self.leapMotionWorker = LeapMotionWorker()
        self.leapMotionWorker.moveToThread(self.thread)

        self.leapMotionWorker.tracking_listener.deviceStatusChanged.connect(
            self.data_management_ui.update_device_status_slot,
            type=Qt.QueuedConnection,
        )

        # Use the tracking_listener from leapMotionWorker
        self.data_management_ui.toggleRecordingSignal.connect(
            self.leapMotionWorker.tracking_listener.toggle_recording_slot,
            type=Qt.QueuedConnection,
        )

        self.data_management_ui.userInfoSubmitted.connect(
            self.leapMotionWorker.tracking_listener.set_filename_info_slot,
            type=Qt.QueuedConnection,
        )

        # Connect the realTimeDataUpdated signal to the DataManagementUI slot for real-time updates
        self.leapMotionWorker.tracking_listener.realTimeDataUpdated.connect(
            self.data_management_ui.update_real_time_data,
            type=Qt.QueuedConnection,
        )

        self.thread.started.connect(self.leapMotionWorker.run)
        self.leapMotionWorker.finished.connect(self.thread.quit)
        self.thread.start()

    def closeEvent(self, event):
        # Signal the worker to stop its loop or work
        self.leapMotionWorker.requestStop()

        # Stop the thread
        self.thread.quit()
        self.thread.wait()

        super().closeEvent(event)


app = QApplication(sys.argv)

window = Application()

window.show()
app.exec()
