from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QMessageBox,
    QLineEdit,
    QDateEdit,
    QTableWidget,
    QTableWidgetItem,
)
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class DataManagementUI(QObject):

    # Custom signal to emit Name, ID, and Date
    userInfoSubmitted = Signal(str, str, str)

    # # Define a new signal for toggling the recording state
    toggleRecordingSignal = Signal(bool)

    def __init__(
        self,
        device_top_status: QLabel,
        device_bottom_status: QLabel,
        device_side_status: QLabel,
        recordButton: QPushButton,
        name_for_csv: QLineEdit,
        id_for_csv: QLineEdit,
        date_for_csv: QDateEdit,
        metacarpal_table: QTableWidget,
        proximal_table: QTableWidget,
        intermediate_table: QTableWidget,
        distal_table: QTableWidget,
        top_view_label: QLabel,
        bottom_view_label: QLabel,
        side_view_label: QLabel,
    ):
        # Initialize QObject
        QObject.__init__(self)  # Initialize QObject

        # Device Connection Initialization
        self.device_top_status = device_top_status
        self.device_bottom_status = device_bottom_status
        self.device_side_status = device_side_status
        self.top_device_id = "LP85571778017"
        self.bottom_device_id = "LP76907386047"
        self.side_device_id = "LP19298121554"

        # Initialize the device connection status dictionary
        self.device_connection_status = {
            "top": False,
            "bottom": False,
            "side": False,
        }

        # Initialize the record button reference and status
        self.record_button = recordButton  # Correctly reference the record button
        self.record_button.clicked.connect(self.record_button_clicked)
        self.is_recording_ui = False

        # Initialize the name, ID, and date fields
        self.name_for_csv = name_for_csv
        self.id_for_csv = id_for_csv
        self.date_for_csv = date_for_csv

        # Initialize the table widgets
        self.metacarpal_table = metacarpal_table
        self.proximal_table = proximal_table
        self.intermediate_table = intermediate_table
        self.distal_table = distal_table

        self.finger_name_to_row = {
            "thumb": 0,
            "index": 1,
            "middle": 2,
            "ring": 3,
            "pinky": 4,
        }
        self.device_id_to_column = {
            "device_1": 0,
            "device_2": 1,
            "device_3": 2,
        }

        # Initialize the view labels
        self.top_view_label = top_view_label
        self.bottom_view_label = bottom_view_label
        self.side_view_label = side_view_label

    ########################################################################################################
    # Device Connection Status Implementation
    ########################################################################################################

    # Method to update a device's connection status
    def update_device_status_slot(self, device_id, is_connected):
        # Assuming device_id is one of the device IDs you're tracking
        # Update the connection status for the appropriate device
        if device_id == self.top_device_id:
            self.device_connection_status["top"] = is_connected
        elif device_id == self.bottom_device_id:
            self.device_connection_status["bottom"] = is_connected
        elif device_id == self.side_device_id:
            self.device_connection_status["side"] = is_connected
        # Update the UI labels accordingly
        self.update_device_status_ui()

    def update_device_status_ui(self):
        # Update the label for each device based on the connection status
        self.device_top_status.setText(
            "Connected" if self.device_connection_status["top"] else "Disconnected"
        )
        self.device_bottom_status.setText(
            "Connected" if self.device_connection_status["bottom"] else "Disconnected"
        )
        self.device_side_status.setText(
            "Connected" if self.device_connection_status["side"] else "Disconnected"
        )
        # Update the label colors based on connection status
        for label, status in zip(
            (
                self.device_top_status,
                self.device_bottom_status,
                self.device_side_status,
            ),
            (
                self.device_connection_status["top"],
                self.device_connection_status["bottom"],
                self.device_connection_status["side"],
            ),
        ):
            label.setStyleSheet(
                "QLabel { color: %s; }" % ("green" if status else "red")
            )

    def check_device_connection_top(self):
        """Check the connection status of the top device."""
        return self.device_connection_status["top"]

    def check_device_connection_bottom(self):
        """Check the connection status of the bottom device."""
        return self.device_connection_status["bottom"]

    def check_device_connection_side(self):
        """Check the connection status of the side device."""
        return self.device_connection_status["side"]

    ########################################################################################################
    # Record Button Implementation
    ########################################################################################################
    def record_button_clicked(self):
        # print("Debug: Record button clicked")
        # Check if all devices are connected
        all_devices_connected = (
            self.check_device_connection_top()
            and self.check_device_connection_bottom()
            and self.check_device_connection_side()
        )

        # Check if the name, id, and date are provided
        name = self.name_for_csv.text().strip()
        id = self.id_for_csv.text().strip()

        if not all_devices_connected:
            # Show message box if not all devices are connected
            QMessageBox.warning(
                None,  # Changed this to None for a standalone message box
                "Device Connection Required",
                "All devices must be connected before recording can start. Please connect all devices.",
            )
            return

        if not name or not id:
            # Show message box if name or ID is missing
            QMessageBox.warning(
                None,  # Changed this to None for a standalone message box
                "Name and ID Required",
                "Please enter your name and ID before starting the recording.",
            )
            return

        # Toggle the recording state BEFORE emitting the signal
        self.is_recording_ui = not self.is_recording_ui

        print(f"Before emitting signal: {self.is_recording_ui}")
        self.toggleRecordingSignal.emit(self.is_recording_ui)
        print("Signal emitted.")

        self.update_record_button_ui(self.is_recording_ui)

        # Emit the userInfoSubmitted signal when recording starts
        if self.is_recording_ui:
            print(
                "Debug: Record button clicked. Checking connections and emitting user info."
            )
            self.emit_user_info()

    def update_record_button_ui(self, is_recording_ui):
        print(f"Updating button status to: {'Stop' if is_recording_ui else 'Start'}")

        # Update record button text and color based on recording status
        if is_recording_ui:
            self.record_button.setText("Stop")
            self.record_button.setStyleSheet(
                "QPushButton { "
                "background-color: rgb(239, 68, 68); "
                "border-style: solid; "
                "border-width: 2px; "
                "border-radius: 10px; "
                "border-color: rgb(239, 68, 68); }"
            )

        else:
            self.record_button.setText("Record")
            self.record_button.setStyleSheet(
                "QPushButton { "
                "background-color: rgb(74, 222, 128); "
                "border-style: solid; "
                "border-width: 2px; "
                "border-radius: 10px; "
                "border-color: rgb(74, 222, 128); }"
            )

    ########################################################################################################
    # Information CSV Implementation
    ########################################################################################################
    def emit_user_info(self):
        name = self.name_for_csv.text()
        id = self.id_for_csv.text()
        date = self.date_for_csv.date().toString("yyyyMMdd")

        # Debug output when user info is emitted
        print(f"Debug: Emitting user info - Name: {name}, ID: {id}, Date: {date}")
        self.userInfoSubmitted.emit(name, id, date)

    #######################################################################################################
    # Real Time View Table Implementation
    #######################################################################################################
    def update_real_time_data(self, data):
        # print("Received data for update:", data)  # Print the received data

        # Maps for converting data to table coordinates
        finger_name_to_row = {
            "thumb": 0,
            "index": 1,
            "middle": 2,
            "ring": 3,
            "pinky": 4,
        }
        device_id_to_column = {
            "device_1": 0,
            "device_2": 1,
            "device_3": 2,
        }  # Update with actual device IDs

        # Extracting information from the data
        finger_name = data["finger_name"]
        bone_name = data["bone_name"]
        device_id = data["device_id"]  # This should match keys in device_id_to_column
        start_x = data["start_x"]

        # Find the correct row and column
        row = finger_name_to_row.get(finger_name, None)
        column = device_id_to_column.get(device_id, None)

        if row is None or column is None:
            print(
                f"Warning: Invalid finger name '{finger_name}' or device ID '{device_id}'. Skipping update."
            )
            return

        # Select the correct table
        if bone_name == "metacarpal":
            table = self.metacarpal_table
        elif bone_name == "proximal":
            table = self.proximal_table
        elif bone_name == "intermediate":
            table = self.intermediate_table
        elif bone_name == "distal":
            table = self.distal_table
        else:
            print(f"Warning: Invalid bone name '{bone_name}'. Skipping update.")
            return

        # Ensure the table widget exists before trying to update it
        if table is not None:
            # Update the table item
            table.setItem(row, column, QTableWidgetItem(str(start_x)))

            # Debug print to confirm the update
            print(
                f"Updated {bone_name} table, {finger_name} row, device {device_id} column with start_x: {start_x}"
            )
        else:
            print(
                "Warning: Attempted to update a non-existent table. Check bone name mappings."
            )

    #######################################################################################################
    # Real Time Skeleton View Implementation
    #######################################################################################################
    @Slot(dict)
    def update_skeleton_view(self, data):
        device_id = data["device_id"]
        qimage = data["image"]

        # Determine which label to update based on the device_id
        if device_id == self.top_device_id:
            label_to_update = self.top_view_label
        elif device_id == self.bottom_device_id:
            label_to_update = self.bottom_view_label
        elif device_id == self.side_device_id:
            label_to_update = self.side_view_label
        else:
            print(f"Warning: Received data for unknown device ID '{device_id}'.")
            return

        # Update the QLabel with the new QImage
        if label_to_update:
            pixmap = QPixmap.fromImage(qimage)
            label_to_update.setPixmap(
                pixmap.scaled(
                    label_to_update.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
            )
        else:
            print(f"Error: No label available to update for device ID '{device_id}'.")
