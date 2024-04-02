# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leapmotion_ver2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QDateEdit,
    QGridLayout,
    QGroupBox,
    QHeaderView,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1280, 720))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.data_management_widget = QWidget(self.centralwidget)
        self.data_management_widget.setObjectName("data_management_widget")
        self.data_management_widget.setMaximumSize(QSize(1871, 151))
        self.data_logger = QGroupBox(self.data_management_widget)
        self.data_logger.setObjectName("data_logger")
        self.data_logger.setGeometry(QRect(470, 10, 231, 131))
        font = QFont()
        font.setFamilies(["Lato Heavy"])
        font.setPointSize(12)
        font.setBold(True)
        self.data_logger.setFont(font)
        self.data_logger.setCheckable(True)
        self.data_logger.setChecked(True)
        self.layoutWidget = QWidget(self.data_logger)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 191, 91))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")
        font1 = QFont()
        font1.setFamilies(["Lato"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.radioButton.setFont(font1)
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(False)

        self.verticalLayout_14.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setFont(font1)
        self.radioButton_2.setChecked(False)

        self.verticalLayout_14.addWidget(self.radioButton_2)

        self.device_connection = QGroupBox(self.data_management_widget)
        self.device_connection.setObjectName("device_connection")
        self.device_connection.setGeometry(QRect(200, 10, 261, 131))
        self.device_connection.setFont(font)
        self.layoutWidget1 = QWidget(self.device_connection)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 23, 231, 101))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.device_top = QLabel(self.layoutWidget1)
        self.device_top.setObjectName("device_top")
        self.device_top.setFont(font1)

        self.verticalLayout_12.addWidget(self.device_top)

        self.device_bottom = QLabel(self.layoutWidget1)
        self.device_bottom.setObjectName("device_bottom")
        self.device_bottom.setFont(font1)

        self.verticalLayout_12.addWidget(self.device_bottom)

        self.device_side_2 = QLabel(self.layoutWidget1)
        self.device_side_2.setObjectName("device_side_2")
        self.device_side_2.setFont(font1)

        self.verticalLayout_12.addWidget(self.device_side_2)

        self.gridLayout_3.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.device_top_status = QLabel(self.layoutWidget1)
        self.device_top_status.setObjectName("device_top_status")
        font2 = QFont()
        font2.setFamilies(["Lato"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.device_top_status.setFont(font2)
        self.device_top_status.setStyleSheet("QLabel{\n" "	color: red;\n" "}")

        self.verticalLayout_13.addWidget(self.device_top_status)

        self.device_bottom_status = QLabel(self.layoutWidget1)
        self.device_bottom_status.setObjectName("device_bottom_status")
        self.device_bottom_status.setFont(font2)
        self.device_bottom_status.setStyleSheet("QLabel{\n" "	color: red;\n" "}")

        self.verticalLayout_13.addWidget(self.device_bottom_status)

        self.device_side_status = QLabel(self.layoutWidget1)
        self.device_side_status.setObjectName("device_side_status")
        self.device_side_status.setFont(font2)
        self.device_side_status.setStyleSheet("QLabel{\n" "	color: red;\n" "}")

        self.verticalLayout_13.addWidget(self.device_side_status)

        self.gridLayout_3.addLayout(self.verticalLayout_13, 0, 1, 1, 1)

        self.saved_data_information = QGroupBox(self.data_management_widget)
        self.saved_data_information.setObjectName("saved_data_information")
        self.saved_data_information.setGeometry(QRect(720, 10, 331, 131))
        self.saved_data_information.setFont(font)
        self.layoutWidget2 = QWidget(self.saved_data_information)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 311, 101))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_name = QLabel(self.layoutWidget2)
        self.label_name.setObjectName("label_name")
        self.label_name.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_name)

        self.label_id = QLabel(self.layoutWidget2)
        self.label_id.setObjectName("label_id")
        self.label_id.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_id)

        self.label_date = QLabel(self.layoutWidget2)
        self.label_date.setObjectName("label_date")
        self.label_date.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_date)

        self.gridLayout_4.addLayout(self.verticalLayout_15, 0, 0, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.name_for_csv = QLineEdit(self.layoutWidget2)
        self.name_for_csv.setObjectName("name_for_csv")
        font3 = QFont()
        font3.setFamilies(["Lato Thin"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.name_for_csv.setFont(font3)

        self.verticalLayout_16.addWidget(self.name_for_csv)

        self.id_for_csv = QLineEdit(self.layoutWidget2)
        self.id_for_csv.setObjectName("id_for_csv")
        self.id_for_csv.setFont(font3)

        self.verticalLayout_16.addWidget(self.id_for_csv)

        self.date_for_csv = QDateEdit(self.layoutWidget2)
        self.date_for_csv.setObjectName("date_for_csv")
        self.date_for_csv.setFont(font3)
        self.date_for_csv.setCalendarPopup(True)

        self.verticalLayout_16.addWidget(self.date_for_csv)

        self.gridLayout_4.addLayout(self.verticalLayout_16, 0, 1, 1, 1)

        self.recordButton = QPushButton(self.data_management_widget)
        self.recordButton.setObjectName("recordButton")
        self.recordButton.setGeometry(QRect(1060, 20, 200, 120))
        self.recordButton.setMinimumSize(QSize(200, 120))
        font4 = QFont()
        font4.setFamilies(["Lato"])
        font4.setPointSize(33)
        font4.setBold(True)
        self.recordButton.setFont(font4)
        self.recordButton.setStyleSheet(
            "QPushButton{\n"
            "	    background-color: rgb(74, 222, 128);\n"
            "        border-style: solid;\n"
            "        border-width: 2px;\n"
            "        border-radius: 10px;  \n"
            "        border-color: rgb(74, 222, 128);\n"
            "}\n"
            "\n"
            "QPushButton:hover {\n"
            "        border-color: #38bdf8;  /* Change border color on hover */\n"
            "}"
        )
        self.recordButton.setCheckable(False)
        self.recordButton.setAutoDefault(False)
        self.logoWTMH = QLabel(self.data_management_widget)
        self.logoWTMH.setObjectName("logoWTMH")
        self.logoWTMH.setGeometry(QRect(30, 10, 120, 120))
        self.logoWTMH.setMinimumSize(QSize(120, 120))
        self.logoWTMH.setPixmap(QPixmap(":/images/images/WTMH.png"))
        self.logoWTMH.setScaledContents(True)

        self.gridLayout_5.addWidget(self.data_management_widget, 0, 0, 1, 1)

        self.data_visualization_widget = QWidget(self.centralwidget)
        self.data_visualization_widget.setObjectName("data_visualization_widget")
        self.data_visualization_widget.setMaximumSize(QSize(1871, 16777215))
        self.real_time_value = QGroupBox(self.data_visualization_widget)
        self.real_time_value.setObjectName("real_time_value")
        self.real_time_value.setGeometry(QRect(0, 0, 1261, 551))
        self.real_time_value.setMaximumSize(QSize(1360, 900))
        font5 = QFont()
        font5.setFamilies(["Lato Heavy"])
        font5.setPointSize(12)
        self.real_time_value.setFont(font5)

        self.joint_static = QWidget(self.real_time_value)
        self.joint_static.setObjectName("joint_static")
        self.joint_static.setGeometry(QRect(10, 30, 661, 820))
        self.joint_static.setMaximumSize(QSize(680, 820))
        self.joint_static.setStyleSheet("")
        self.layoutWidget3 = QWidget(self.joint_static)
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(0, 0, 661, 501))
        self.verticalLayout_19 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.joint_static_label = QLabel(self.layoutWidget3)
        self.joint_static_label.setObjectName("joint_static_label")
        self.joint_static_label.setMaximumSize(QSize(210, 30))
        font6 = QFont()
        font6.setFamilies(["Lato Thin"])
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setUnderline(True)
        self.joint_static_label.setFont(font6)
        self.joint_static_label.setStyleSheet("")

        self.verticalLayout_19.addWidget(self.joint_static_label)

        ##############################################################################################################
        # Metacarpal Table
        ##############################################################################################################

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.metacarpal_label = QLabel(self.layoutWidget3)
        self.metacarpal_label.setObjectName("metacarpal_label")

        font7 = QFont()
        font7.setFamilies(["Lato"])
        font7.setPointSize(12)
        self.metacarpal_label.setFont(font7)

        self.verticalLayout.addWidget(self.metacarpal_label)

        self.metacarpal_table = QTableWidget(self.layoutWidget3)
        self.metacarpal_table.setColumnCount(3)
        self.metacarpal_table.setRowCount(5)

        # Set header labels for device (columns) and fingers (rows)
        self.metacarpal_table.setHorizontalHeaderLabels(
            ["Device 1", "Device 2", "Device 3"]
        )
        self.metacarpal_table.setVerticalHeaderLabels(
            ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        )
        font9 = QFont()
        font9.setFamilies(["Lato"])
        font9.setPointSize(9)
        self.metacarpal_table.setFont(font9)

        # Configure table properties
        self.metacarpal_table.horizontalHeader().setMinimumSectionSize(32)
        self.metacarpal_table.horizontalHeader().setDefaultSectionSize(91)
        self.metacarpal_table.verticalHeader().setMinimumSectionSize(23)
        self.metacarpal_table.verticalHeader().setDefaultSectionSize(35)

        # Optionally, initialize cells with empty items to enable easier updating
        for row in range(self.metacarpal_table.rowCount()):
            for column in range(self.metacarpal_table.columnCount()):
                item = QTableWidgetItem("0")
                item.setTextAlignment(Qt.AlignCenter)
                self.metacarpal_table.setItem(row, column, item)

        # Add the table to the layout
        self.verticalLayout.addWidget(self.metacarpal_table)

        ##############################################################################################################
        # Proximal Table
        ##############################################################################################################

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.proximal_label = QLabel(self.layoutWidget3)
        self.proximal_label.setObjectName("proximal_label")
        self.proximal_label.setFont(font7)

        self.verticalLayout_2.addWidget(self.proximal_label)

        # Initialization of the proximal_table similar to metacarpal_table
        self.proximal_table = QTableWidget(self.layoutWidget3)
        self.proximal_table.setColumnCount(3)
        self.proximal_table.setRowCount(5)

        # Set header labels for clarity
        self.proximal_table.setHorizontalHeaderLabels(
            ["Device 1", "Device 2", "Device 3"]
        )
        self.proximal_table.setVerticalHeaderLabels(
            ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        )

        # Optionally set font for the table
        font = QFont()
        font.setFamily("Lato")
        font.setPointSize(9)
        self.proximal_table.setFont(font)

        # Set default section sizes for headers
        self.proximal_table.horizontalHeader().setMinimumSectionSize(32)
        self.proximal_table.horizontalHeader().setDefaultSectionSize(91)
        self.proximal_table.verticalHeader().setMinimumSectionSize(23)
        self.proximal_table.verticalHeader().setDefaultSectionSize(35)

        # Initialize all cells with "0" and align text to center
        for row in range(self.proximal_table.rowCount()):
            for column in range(self.proximal_table.columnCount()):
                item = QTableWidgetItem("0")  # Set initial value to "0"
                item.setTextAlignment(Qt.AlignCenter)  # Align the text to center
                self.proximal_table.setItem(row, column, item)

        self.verticalLayout_2.addWidget(self.proximal_table)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        ##############################################################################################################
        # Intermediate Table
        ##############################################################################################################

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.intermediate_label = QLabel(self.layoutWidget3)
        self.intermediate_label.setObjectName("intermediate_label")
        self.intermediate_label.setFont(font7)

        self.verticalLayout_3.addWidget(self.intermediate_label)

        # Initialization of the proximal_table similar to metacarpal_table
        self.intermediate_table = QTableWidget(self.layoutWidget3)
        self.intermediate_table.setColumnCount(
            3
        )  # For Device 1, Device 2, and Device 3
        self.intermediate_table.setRowCount(5)  # For Thumb, Index, Middle, Ring, Pinky

        # Set header labels for clarity
        self.intermediate_table.setHorizontalHeaderLabels(
            ["Device 1", "Device 2", "Device 3"]
        )
        self.intermediate_table.setVerticalHeaderLabels(
            ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        )

        # Optionally set font for the table
        font = QFont()
        font.setFamily("Lato")
        font.setPointSize(9)
        self.intermediate_table.setFont(font)

        # Set default section sizes for headers
        self.intermediate_table.horizontalHeader().setMinimumSectionSize(32)
        self.intermediate_table.horizontalHeader().setDefaultSectionSize(91)
        self.intermediate_table.verticalHeader().setMinimumSectionSize(23)
        self.intermediate_table.verticalHeader().setDefaultSectionSize(35)

        # Initialize all cells with "0" and align text to center
        for row in range(self.intermediate_table.rowCount()):
            for column in range(self.intermediate_table.columnCount()):
                item = QTableWidgetItem("0")  # Set initial value to "0"
                item.setTextAlignment(Qt.AlignCenter)  # Align the text to center
                self.intermediate_table.setItem(row, column, item)

        self.verticalLayout_3.addWidget(self.intermediate_table)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        ##############################################################################################################
        # Distal Table
        ##############################################################################################################

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.distal_label = QLabel(self.layoutWidget3)
        self.distal_label.setObjectName("distal_label")
        self.distal_label.setFont(font7)

        self.verticalLayout_4.addWidget(self.distal_label)

        # Initialization of the proximal_table similar to metacarpal_table
        self.distal_table = QTableWidget(self.layoutWidget3)
        self.distal_table.setColumnCount(3)  # For Device 1, Device 2, and Device 3
        self.distal_table.setRowCount(5)  # For Thumb, Index, Middle, Ring, Pinky

        # Set header labels for clarity
        self.distal_table.setHorizontalHeaderLabels(
            ["Device 1", "Device 2", "Device 3"]
        )
        self.distal_table.setVerticalHeaderLabels(
            ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        )

        # Optionally set font for the table
        font = QFont()
        font.setFamily("Lato")
        font.setPointSize(9)
        self.distal_table.setFont(font)

        # Set default section sizes for headers
        self.distal_table.horizontalHeader().setMinimumSectionSize(32)
        self.distal_table.horizontalHeader().setDefaultSectionSize(91)
        self.distal_table.verticalHeader().setMinimumSectionSize(23)
        self.distal_table.verticalHeader().setDefaultSectionSize(35)

        # Initialize all cells with "0" and align text to center
        for row in range(self.distal_table.rowCount()):
            for column in range(self.distal_table.columnCount()):
                item = QTableWidgetItem("0")  # Set initial value to "0"
                item.setTextAlignment(Qt.AlignCenter)  # Align the text to center
                self.distal_table.setItem(row, column, item)

        self.verticalLayout_4.addWidget(self.distal_table)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 1, 1, 1)

        ##############################################################################################################

        self.verticalLayout_19.addLayout(self.gridLayout_2)

        self.angle_of_joint = QWidget(self.real_time_value)
        self.angle_of_joint.setObjectName("angle_of_joint")
        self.angle_of_joint.setGeometry(QRect(690, 30, 661, 820))
        self.angle_of_joint.setMaximumSize(QSize(680, 820))
        self.angle_of_joint.setStyleSheet("")
        self.real_time_skeleton_view = QGroupBox(self.angle_of_joint)
        self.real_time_skeleton_view.setObjectName("real_time_skeleton_view")
        self.real_time_skeleton_view.setGeometry(QRect(-10, -20, 0, 0))
        self.real_time_skeleton_view.setMaximumSize(QSize(1920, 1080))
        font10 = QFont()
        font10.setFamilies(["Lato Heavy"])
        font10.setPointSize(12)
        font10.setBold(False)
        self.real_time_skeleton_view.setFont(font10)
        self.layoutWidget4 = QWidget(self.angle_of_joint)
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(0, 0, 571, 511))
        self.gridLayout = QGridLayout(self.layoutWidget4)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_32 = QLabel(self.layoutWidget4)
        self.label_32.setObjectName("label_32")
        font11 = QFont()
        font11.setFamilies(["Lato Thin"])
        font11.setPointSize(18)
        font11.setBold(False)
        self.label_32.setFont(font11)

        self.verticalLayout_11.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.label_33 = QLabel(self.layoutWidget4)
        self.label_33.setObjectName("label_33")
        self.label_33.setStyleSheet("QVBoxLayout{\n" "	text-align:left;\n" "}")
        self.label_33.setPixmap(
            QPixmap(":/images/images/Screenshot 2024-03-27 173518.png")
        )
        self.label_33.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_33)

        self.gridLayout.addLayout(self.verticalLayout_11, 2, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_16 = QLabel(self.layoutWidget4)
        self.label_16.setObjectName("label_16")
        self.label_16.setFont(font11)

        self.verticalLayout_10.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.label_31 = QLabel(self.layoutWidget4)
        self.label_31.setObjectName("label_31")
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet("QVBoxLayout{\n" "	text-align:left;\n" "}")
        self.label_31.setPixmap(
            QPixmap(":/images/images/Screenshot 2024-03-27 173518.png")
        )
        self.label_31.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_31)

        self.gridLayout.addLayout(self.verticalLayout_10, 1, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label = QLabel(self.layoutWidget4)
        self.label.setObjectName("label")
        self.label.setFont(font11)

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.layoutWidget4)
        self.label_15.setObjectName("label_15")
        font12 = QFont()
        font12.setFamilies(["Lato"])
        font12.setPointSize(9)
        font12.setBold(False)
        self.label_15.setFont(font12)
        self.label_15.setStyleSheet("QVBoxLayout{\n" "	text-align:left;\n" "}")
        self.label_15.setPixmap(
            QPixmap(":/images/images/Screenshot 2024-03-27 173518.png")
        )
        self.label_15.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_15)

        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.gridLayout_5.addWidget(self.data_visualization_widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.data_logger.setTitle(
            QCoreApplication.translate("MainWindow", "Enable Data Logger", None)
        )
        self.radioButton.setText(
            QCoreApplication.translate("MainWindow", "New Data", None)
        )
        self.radioButton_2.setText(
            QCoreApplication.translate("MainWindow", "Overwrite", None)
        )
        self.device_connection.setTitle(
            QCoreApplication.translate("MainWindow", "Device Connection", None)
        )
        self.device_top.setText(
            QCoreApplication.translate("MainWindow", "Device Top:", None)
        )
        self.device_bottom.setText(
            QCoreApplication.translate("MainWindow", "Device Bottom:", None)
        )
        self.device_side_2.setText(
            QCoreApplication.translate("MainWindow", "Device Side:", None)
        )
        self.device_top_status.setText(
            QCoreApplication.translate("MainWindow", "Disconnected", None)
        )
        self.device_bottom_status.setText(
            QCoreApplication.translate("MainWindow", "Disconnected", None)
        )
        self.device_side_status.setText(
            QCoreApplication.translate("MainWindow", "Disconnected", None)
        )
        self.saved_data_information.setTitle(
            QCoreApplication.translate("MainWindow", "Information", None)
        )
        self.label_name.setText(QCoreApplication.translate("MainWindow", "Name:", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", "ID:", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", "Date:", None))
        self.recordButton.setText(
            QCoreApplication.translate("MainWindow", "Record", None)
        )
        self.logoWTMH.setText("")
        self.real_time_value.setTitle(
            QCoreApplication.translate("MainWindow", "Real Time Value", None)
        )
        self.joint_static_label.setText(
            QCoreApplication.translate("MainWindow", "Joint Static", None)
        )
        self.metacarpal_label.setText(
            QCoreApplication.translate("MainWindow", "Metacarpal", None)
        )

        self.proximal_label.setText(
            QCoreApplication.translate("MainWindow", "Proximal", None)
        )

        self.intermediate_label.setText(
            QCoreApplication.translate("MainWindow", "Intermediate", None)
        )

        self.distal_label.setText(
            QCoreApplication.translate("MainWindow", "Distal", None)
        )

        self.real_time_skeleton_view.setTitle(
            QCoreApplication.translate("MainWindow", "Real Time Skeleton View", None)
        )
        self.label_32.setText(
            QCoreApplication.translate("MainWindow", "Side View", None)
        )
        self.label_33.setText("")
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "Bottom View", None)
        )
        self.label_31.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", "Top View", None))
        self.label_15.setText("")

    # retranslateUi
