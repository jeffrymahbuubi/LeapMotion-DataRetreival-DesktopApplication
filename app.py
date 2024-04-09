from PySide6.QtWidgets import QMainWindow, QApplication
from PySide6.QtCore import QThread, Qt, QTimer
from PySide6.QtGui import QIcon
import sys
from leapmotion_ver3 import Ui_MainWindow
from data_management_ui import DataManagementUI
from leapmotion_logic import TrackingEventListener, LeapMotionWorker


class Application(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Leap Motion Gemini V1.0")
        self.setWindowIcon(QIcon("images/WTMH.ico"))

        # Delay further initialization
        QTimer.singleShot(2000, self.delayedInit)  # Delay of 1000 ms (1 second)

    def delayedInit(self):
        # This method will be called after the specified delay
        self.tracking_listener = TrackingEventListener()

        # Setup DataManagementUI and connections
        self.setupDataManagementUI()

        # Start Leap Motion in a separate thread
        self.start_leap_motion_thread()

    def setupDataManagementUI(self):
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
            self.top_view_label,
            self.bottom_view_label,
            self.side_view_label,
        )

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

        print("Connecting imageUpdated signal to update_skeleton_view slot.")
        # Connect the imageUpdated signal to update the skeleton view in the UI
        self.leapMotionWorker.tracking_listener.imageUpdated.connect(
            self.data_management_ui.update_skeleton_view,
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
