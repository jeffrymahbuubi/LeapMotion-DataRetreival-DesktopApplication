# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leapmotion_ver3.ui'
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
    QHBoxLayout,
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
        MainWindow.setMinimumSize(QSize(1280, 768))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_6 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.data_management_widget = QWidget(self.centralwidget)
        self.data_management_widget.setObjectName("data_management_widget")
        self.data_management_widget.setMaximumSize(QSize(1920, 150))
        self.horizontalLayout = QHBoxLayout(self.data_management_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.logoWTMH = QLabel(self.data_management_widget)
        self.logoWTMH.setObjectName("logoWTMH")
        self.logoWTMH.setMinimumSize(QSize(120, 120))
        self.logoWTMH.setMaximumSize(QSize(120, 120))
        self.logoWTMH.setPixmap(QPixmap(":/images/images/WTMH.png"))
        self.logoWTMH.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logoWTMH)

        self.device_connection = QGroupBox(self.data_management_widget)
        self.device_connection.setObjectName("device_connection")
        self.device_connection.setMinimumSize(QSize(232, 133))
        font = QFont()
        font.setFamilies(["Lato Heavy"])
        font.setPointSize(12)
        font.setBold(True)
        self.device_connection.setFont(font)
        self.horizontalLayout_2 = QHBoxLayout(self.device_connection)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.device_top = QLabel(self.device_connection)
        self.device_top.setObjectName("device_top")
        font1 = QFont()
        font1.setFamilies(["Lato"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.device_top.setFont(font1)

        self.verticalLayout_12.addWidget(self.device_top)

        self.device_bottom = QLabel(self.device_connection)
        self.device_bottom.setObjectName("device_bottom")
        self.device_bottom.setFont(font1)

        self.verticalLayout_12.addWidget(self.device_bottom)

        self.device_side_2 = QLabel(self.device_connection)
        self.device_side_2.setObjectName("device_side_2")
        self.device_side_2.setFont(font1)

        self.verticalLayout_12.addWidget(self.device_side_2)

        self.gridLayout_3.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.device_top_status = QLabel(self.device_connection)
        self.device_top_status.setObjectName("device_top_status")
        font2 = QFont()
        font2.setFamilies(["Lato"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.device_top_status.setFont(font2)
        self.device_top_status.setStyleSheet("QLabel{\n" "	color: red;\n" "}")

        self.verticalLayout_13.addWidget(self.device_top_status)

        self.device_bottom_status = QLabel(self.device_connection)
        self.device_bottom_status.setObjectName("device_bottom_status")
        self.device_bottom_status.setFont(font2)
        self.device_bottom_status.setStyleSheet("QLabel{\n" "	color: red;\n" "}")

        self.verticalLayout_13.addWidget(self.device_bottom_status)

        self.device_side_status = QLabel(self.device_connection)
        self.device_side_status.setObjectName("device_side_status")
        self.device_side_status.setFont(font2)
        self.device_side_status.setStyleSheet("QLabel{\n" "	color: red;\n" "}")

        self.verticalLayout_13.addWidget(self.device_side_status)

        self.gridLayout_3.addLayout(self.verticalLayout_13, 0, 1, 1, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout_3)

        self.horizontalLayout.addWidget(self.device_connection)

        self.data_logger = QGroupBox(self.data_management_widget)
        self.data_logger.setObjectName("data_logger")
        self.data_logger.setMinimumSize(QSize(232, 133))
        self.data_logger.setFont(font)
        self.data_logger.setCheckable(True)
        self.data_logger.setChecked(True)
        self.horizontalLayout_3 = QHBoxLayout(self.data_logger)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.radioButton = QRadioButton(self.data_logger)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setFont(font1)
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(False)

        self.verticalLayout_14.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.data_logger)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setFont(font1)
        self.radioButton_2.setChecked(False)

        self.verticalLayout_14.addWidget(self.radioButton_2)

        self.horizontalLayout_3.addLayout(self.verticalLayout_14)

        self.horizontalLayout.addWidget(self.data_logger)

        self.saved_data_information = QGroupBox(self.data_management_widget)
        self.saved_data_information.setObjectName("saved_data_information")
        self.saved_data_information.setMinimumSize(QSize(232, 133))
        self.saved_data_information.setFont(font)
        self.horizontalLayout_4 = QHBoxLayout(self.saved_data_information)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_name = QLabel(self.saved_data_information)
        self.label_name.setObjectName("label_name")
        self.label_name.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_name)

        self.label_id = QLabel(self.saved_data_information)
        self.label_id.setObjectName("label_id")
        self.label_id.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_id)

        self.label_date = QLabel(self.saved_data_information)
        self.label_date.setObjectName("label_date")
        self.label_date.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_date)

        self.gridLayout_4.addLayout(self.verticalLayout_15, 0, 0, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.name_for_csv = QLineEdit(self.saved_data_information)
        self.name_for_csv.setObjectName("name_for_csv")
        font3 = QFont()
        font3.setFamilies(["Lato Thin"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.name_for_csv.setFont(font3)

        self.verticalLayout_16.addWidget(self.name_for_csv)

        self.id_for_csv = QLineEdit(self.saved_data_information)
        self.id_for_csv.setObjectName("id_for_csv")
        self.id_for_csv.setFont(font3)

        self.verticalLayout_16.addWidget(self.id_for_csv)

        self.date_for_csv = QDateEdit(self.saved_data_information)
        self.date_for_csv.setObjectName("date_for_csv")
        self.date_for_csv.setFont(font3)
        self.date_for_csv.setCalendarPopup(True)

        self.verticalLayout_16.addWidget(self.date_for_csv)

        self.gridLayout_4.addLayout(self.verticalLayout_16, 0, 1, 1, 1)

        self.horizontalLayout_4.addLayout(self.gridLayout_4)

        self.horizontalLayout.addWidget(self.saved_data_information)

        self.recordButton = QPushButton(self.data_management_widget)
        self.recordButton.setObjectName("recordButton")
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

        self.horizontalLayout.addWidget(self.recordButton)

        self.verticalLayout_6.addWidget(self.data_management_widget)

        self.data_visualization_widget = QWidget(self.centralwidget)
        self.data_visualization_widget.setObjectName("data_visualization_widget")
        self.data_visualization_widget.setMinimumSize(QSize(1262, 577))
        self.data_visualization_widget.setMaximumSize(QSize(1920, 1080))
        self.horizontalLayout_5 = QHBoxLayout(self.data_visualization_widget)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.real_time_value = QGroupBox(self.data_visualization_widget)
        self.real_time_value.setObjectName("real_time_value")
        self.real_time_value.setMaximumSize(QSize(1920, 900))
        font5 = QFont()
        font5.setFamilies(["Lato Heavy"])
        font5.setPointSize(12)
        self.real_time_value.setFont(font5)
        self.horizontalLayout_6 = QHBoxLayout(self.real_time_value)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.joint_static = QWidget(self.real_time_value)
        self.joint_static.setObjectName("joint_static")
        self.joint_static.setMinimumSize(QSize(630, 520))
        self.joint_static.setMaximumSize(QSize(960, 845))
        self.joint_static.setStyleSheet("")
        self.gridLayout = QGridLayout(self.joint_static)
        self.gridLayout.setObjectName("gridLayout")
        self.joint_static_label = QLabel(self.joint_static)
        self.joint_static_label.setObjectName("joint_static_label")
        self.joint_static_label.setMaximumSize(QSize(210, 30))
        font6 = QFont()
        font6.setFamilies(["Lato Thin"])
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setUnderline(True)
        self.joint_static_label.setFont(font6)
        self.joint_static_label.setStyleSheet("")

        self.gridLayout.addWidget(self.joint_static_label, 0, 0, 1, 1)

        ##############################################################################################################
        # Metacarpal Table
        ##############################################################################################################

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.metacarpal_label = QLabel(self.joint_static)
        self.metacarpal_label.setObjectName("metacarpal_label")
        font7 = QFont()
        font7.setFamilies(["Lato"])
        font7.setPointSize(12)
        self.metacarpal_label.setFont(font7)

        self.verticalLayout.addWidget(self.metacarpal_label)

        self.metacarpal_table = QTableWidget(self.joint_static)

        self.metacarpal_table.setObjectName("metacarpal_table")
        self.metacarpal_table.setColumnCount(3)
        self.metacarpal_table.setRowCount(5)

        # Set header labesl for column and rows
        self.metacarpal_table.setHorizontalHeaderLabels(
            ["Device 1", "Device 2", "Device 3"]
        )
        self.metacarpal_table.setVerticalHeaderLabels(
            ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        )

        # Apply font settings
        font9 = QFont()
        font9.setFamilies(["Lato"])
        font9.setPointSize(9)
        self.metacarpal_table.setFont(font9)

        # Configure header properties
        self.metacarpal_table.horizontalHeader().setMinimumSectionSize(32)
        self.metacarpal_table.horizontalHeader().setDefaultSectionSize(91)
        self.metacarpal_table.verticalHeader().setMinimumSectionSize(23)
        self.metacarpal_table.verticalHeader().setDefaultSectionSize(35)

        # Initialize cells with empty items for easier updating
        for row in range(self.metacarpal_table.rowCount()):
            for column in range(self.metacarpal_table.columnCount()):
                item = QTableWidgetItem("0")
                item.setTextAlignment(Qt.AlignCenter)
                self.metacarpal_table.setItem(row, column, item)

        # Set minimum size and configure section resize properties, similar to the reference
        self.metacarpal_table.setMinimumSize(QSize(345, 203))
        self.metacarpal_table.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout.addWidget(self.metacarpal_table)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        ##############################################################################################################
        # Proximal Table
        ##############################################################################################################

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.proximal_label = QLabel(self.joint_static)
        self.proximal_label.setObjectName("proximal_label")
        self.proximal_label.setFont(font7)

        self.verticalLayout_2.addWidget(self.proximal_label)

        self.proximal_table = QTableWidget(self.joint_static)
        self.proximal_table.setObjectName("metacarpal_table")
        self.proximal_table.setColumnCount(3)
        self.proximal_table.setRowCount(5)

        # Set header labels for columns and rows
        self.proximal_table.setHorizontalHeaderLabels(
            ["Device 1", "Device 2", "Device 3"]
        )
        self.proximal_table.setVerticalHeaderLabels(
            ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        )

        # Apply font settings
        font9 = QFont()
        font9.setFamilies(["Lato"])
        font9.setPointSize(9)
        self.metacarpal_table.setFont(font9)

        # Configure header properties
        self.proximal_table.horizontalHeader().setMinimumSectionSize(32)
        self.proximal_table.horizontalHeader().setDefaultSectionSize(91)
        self.proximal_table.verticalHeader().setMinimumSectionSize(23)
        self.proximal_table.verticalHeader().setDefaultSectionSize(35)

        # Initialize cells with empty items for easier updating
        for row in range(self.proximal_table.rowCount()):
            for column in range(self.proximal_table.columnCount()):
                item = QTableWidgetItem("0")
                item.setTextAlignment(Qt.AlignCenter)
                self.proximal_table.setItem(row, column, item)

        # Set minimum size and configure section resize properties, similar to the reference
        self.proximal_table.setMinimumSize(QSize(345, 203))
        self.proximal_table.horizontalHeader().setCascadingSectionResizes(False)

        # Add the table to the layout
        self.verticalLayout_2.addWidget(self.proximal_table)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        ##############################################################################################################
        # Intermediate Table
        ##############################################################################################################

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.intermediate_label = QLabel(self.joint_static)
        self.intermediate_label.setObjectName("intermediate_label")
        self.intermediate_label.setFont(font7)

        self.verticalLayout_3.addWidget(self.intermediate_label)

        self.intermediate_table = QTableWidget(self.joint_static)

        self.intermediate_table.setObjectName("intermediate_table")
        self.intermediate_table.setColumnCount(3)
        self.intermediate_table.setRowCount(5)

        # Set header labels for columns and rows
        self.intermediate_table.setHorizontalHeaderLabels(
            ["Device 1", "Device 2", "Device 3"]
        )
        self.intermediate_table.setVerticalHeaderLabels(
            ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        )

        # Apply font settings
        font9 = QFont()
        font9.setFamilies(["Lato"])
        font9.setPointSize(9)
        self.intermediate_table.setFont(font9)

        # Configure header properties
        self.intermediate_table.horizontalHeader().setMinimumSectionSize(32)
        self.intermediate_table.horizontalHeader().setDefaultSectionSize(91)
        self.intermediate_table.verticalHeader().setMinimumSectionSize(23)
        self.intermediate_table.verticalHeader().setDefaultSectionSize(35)

        # Initialize cells with empty items for easier updating
        for row in range(self.intermediate_table.rowCount()):
            for column in range(self.intermediate_table.columnCount()):
                item = QTableWidgetItem("0")
                item.setTextAlignment(Qt.AlignCenter)
                self.intermediate_table.setItem(row, column, item)

        # Set minimum size and configure section resize properties, similar to the reference
        self.intermediate_table.setMinimumSize(QSize(345, 203))
        self.intermediate_table.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_3.addWidget(self.intermediate_table)
        self.gridLayout.addLayout(self.verticalLayout_3, 2, 0, 1, 1)

        ##############################################################################################################
        # Distal Table
        ##############################################################################################################

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.distal_label = QLabel(self.joint_static)
        self.distal_label.setObjectName("distal_label")
        self.distal_label.setFont(font7)

        self.verticalLayout_4.addWidget(self.distal_label)

        self.distal_table = QTableWidget(self.joint_static)

        self.distal_table.setObjectName("distal_table")
        self.distal_table.setColumnCount(3)
        self.distal_table.setRowCount(5)

        # Set header labels for columns and rows
        self.distal_table.setHorizontalHeaderLabels(
            ["Device 1", "Device 2", "Device 3"]
        )

        self.distal_table.setVerticalHeaderLabels(
            ["Thumb", "Index", "Middle", "Ring", "Pinky"]
        )

        # Apply font settings
        font9 = QFont()
        font9.setFamilies(["Lato"])
        font9.setPointSize(9)
        self.distal_table.setFont(font9)

        # Configure header properties
        self.distal_table.horizontalHeader().setMinimumSectionSize(32)
        self.distal_table.horizontalHeader().setDefaultSectionSize(91)
        self.distal_table.verticalHeader().setMinimumSectionSize(23)
        self.distal_table.verticalHeader().setDefaultSectionSize(35)

        # Initialize cells with empty items for easier updating
        for row in range(self.distal_table.rowCount()):
            for column in range(self.distal_table.columnCount()):
                item = QTableWidgetItem("0")
                item.setTextAlignment(Qt.AlignCenter)
                self.distal_table.setItem(row, column, item)

        # Set minimum size and configure section resize properties, similar to the reference
        self.distal_table.setMinimumSize(QSize(345, 203))
        self.distal_table.horizontalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_4.addWidget(self.distal_table)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 1, 1, 1)

        ##############################################################################################################

        self.horizontalLayout_6.addWidget(self.joint_static)

        self.skeleton_view = QWidget(self.real_time_value)
        self.skeleton_view.setObjectName("skeleton_view")
        self.skeleton_view.setMinimumSize(QSize(500, 520))
        self.skeleton_view.setMaximumSize(QSize(960, 845))
        self.skeleton_view.setStyleSheet("")
        self.verticalLayout_8 = QVBoxLayout(self.skeleton_view)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.skeleton_view_label = QLabel(self.skeleton_view)
        self.skeleton_view_label.setObjectName("skeleton_view_label")
        self.skeleton_view_label.setMaximumSize(QSize(210, 30))
        self.skeleton_view_label.setFont(font6)
        self.skeleton_view_label.setStyleSheet("")

        self.verticalLayout_8.addWidget(self.skeleton_view_label)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.top_view_title = QLabel(self.skeleton_view)
        self.top_view_title.setObjectName("top_view_title")
        font10 = QFont()
        font10.setFamilies(["Lato Thin"])
        font10.setPointSize(18)
        font10.setBold(False)
        self.top_view_title.setFont(font10)

        self.verticalLayout_5.addWidget(self.top_view_title)

        self.top_view_label = QLabel(self.skeleton_view)
        self.top_view_label.setObjectName("top_view_label")
        font11 = QFont()
        font11.setFamilies(["Lato"])
        font11.setPointSize(9)
        font11.setBold(False)
        self.top_view_label.setFont(font11)
        self.top_view_label.setStyleSheet("QVBoxLayout{\n" "	text-align:left;\n" "}")
        self.top_view_label.setPixmap(
            QPixmap(":/images/images/Screenshot 2024-03-27 173518.png")
        )
        self.top_view_label.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.top_view_label)

        self.verticalLayout_8.addLayout(self.verticalLayout_5)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.bottom_view_title = QLabel(self.skeleton_view)
        self.bottom_view_title.setObjectName("bottom_view_title")
        self.bottom_view_title.setFont(font10)

        self.verticalLayout_10.addWidget(self.bottom_view_title)

        self.bottom_view_label = QLabel(self.skeleton_view)
        self.bottom_view_label.setObjectName("bottom_view_label")
        self.bottom_view_label.setFont(font1)
        self.bottom_view_label.setStyleSheet("QVBoxLayout{\n" "	text-align:left;\n" "}")
        self.bottom_view_label.setPixmap(
            QPixmap(":/images/images/Screenshot 2024-03-27 173518.png")
        )
        self.bottom_view_label.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.bottom_view_label)

        self.verticalLayout_8.addLayout(self.verticalLayout_10)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.side_view_title = QLabel(self.skeleton_view)
        self.side_view_title.setObjectName("side_view_title")
        self.side_view_title.setFont(font10)

        self.verticalLayout_11.addWidget(self.side_view_title)

        self.side_view_label = QLabel(self.skeleton_view)
        self.side_view_label.setObjectName("side_view_label")
        self.side_view_label.setStyleSheet("QVBoxLayout{\n" "	text-align:left;\n" "}")
        self.side_view_label.setPixmap(
            QPixmap(":/images/images/Screenshot 2024-03-27 173518.png")
        )
        self.side_view_label.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.side_view_label)

        self.verticalLayout_8.addLayout(self.verticalLayout_11)

        self.horizontalLayout_6.addWidget(self.skeleton_view)

        self.horizontalLayout_5.addWidget(self.real_time_value)

        self.verticalLayout_6.addWidget(self.data_visualization_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.logoWTMH.setText("")
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
        self.data_logger.setTitle(
            QCoreApplication.translate("MainWindow", "Enable Data Logger", None)
        )
        self.radioButton.setText(
            QCoreApplication.translate("MainWindow", "New Data", None)
        )
        self.radioButton_2.setText(
            QCoreApplication.translate("MainWindow", "Overwrite", None)
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

        self.skeleton_view_label.setText(
            QCoreApplication.translate("MainWindow", "Skeleton View", None)
        )
        self.top_view_title.setText(
            QCoreApplication.translate("MainWindow", "Top View", None)
        )
        self.top_view_label.setText("")
        self.bottom_view_title.setText(
            QCoreApplication.translate("MainWindow", "Bottom View", None)
        )
        self.bottom_view_label.setText("")
        self.side_view_title.setText(
            QCoreApplication.translate("MainWindow", "Side View", None)
        )
        self.side_view_label.setText("")

    # retranslateUi
