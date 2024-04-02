# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'leapmotion.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QRadioButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QSize(1706, 1072))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_5 = QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.data_management_widget = QWidget(self.centralwidget)
        self.data_management_widget.setObjectName(u"data_management_widget")
        self.data_management_widget.setMaximumSize(QSize(1871, 151))
        self.data_logger = QGroupBox(self.data_management_widget)
        self.data_logger.setObjectName(u"data_logger")
        self.data_logger.setGeometry(QRect(480, 10, 231, 131))
        font = QFont()
        font.setFamilies([u"Lato Heavy"])
        font.setPointSize(12)
        font.setBold(True)
        self.data_logger.setFont(font)
        self.data_logger.setCheckable(True)
        self.data_logger.setChecked(True)
        self.layoutWidget = QWidget(self.data_logger)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 30, 191, 91))
        self.verticalLayout_14 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName(u"radioButton")
        font1 = QFont()
        font1.setFamilies([u"Lato"])
        font1.setPointSize(12)
        font1.setBold(False)
        self.radioButton.setFont(font1)
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(True)
        self.radioButton.setAutoExclusive(False)

        self.verticalLayout_14.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.layoutWidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setFont(font1)

        self.verticalLayout_14.addWidget(self.radioButton_2)

        self.device_connection = QGroupBox(self.data_management_widget)
        self.device_connection.setObjectName(u"device_connection")
        self.device_connection.setGeometry(QRect(200, 10, 261, 131))
        self.device_connection.setFont(font)
        self.layoutWidget1 = QWidget(self.device_connection)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 23, 231, 101))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.device_top = QLabel(self.layoutWidget1)
        self.device_top.setObjectName(u"device_top")
        self.device_top.setFont(font1)

        self.verticalLayout_12.addWidget(self.device_top)

        self.device_bottom = QLabel(self.layoutWidget1)
        self.device_bottom.setObjectName(u"device_bottom")
        self.device_bottom.setFont(font1)

        self.verticalLayout_12.addWidget(self.device_bottom)

        self.device_side_2 = QLabel(self.layoutWidget1)
        self.device_side_2.setObjectName(u"device_side_2")
        self.device_side_2.setFont(font1)

        self.verticalLayout_12.addWidget(self.device_side_2)


        self.gridLayout_3.addLayout(self.verticalLayout_12, 0, 0, 1, 1)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.device_top_status = QLabel(self.layoutWidget1)
        self.device_top_status.setObjectName(u"device_top_status")
        font2 = QFont()
        font2.setFamilies([u"Lato"])
        font2.setPointSize(11)
        font2.setBold(False)
        self.device_top_status.setFont(font2)
        self.device_top_status.setStyleSheet(u"QLabel{\n"
"	color: red;\n"
"}")

        self.verticalLayout_13.addWidget(self.device_top_status)

        self.device_bottom_status = QLabel(self.layoutWidget1)
        self.device_bottom_status.setObjectName(u"device_bottom_status")
        self.device_bottom_status.setFont(font2)
        self.device_bottom_status.setStyleSheet(u"QLabel{\n"
"	color: red;\n"
"}")

        self.verticalLayout_13.addWidget(self.device_bottom_status)

        self.device_side_status = QLabel(self.layoutWidget1)
        self.device_side_status.setObjectName(u"device_side_status")
        self.device_side_status.setFont(font2)
        self.device_side_status.setStyleSheet(u"QLabel{\n"
"	color: red;\n"
"}")

        self.verticalLayout_13.addWidget(self.device_side_status)


        self.gridLayout_3.addLayout(self.verticalLayout_13, 0, 1, 1, 1)

        self.saved_data_information = QGroupBox(self.data_management_widget)
        self.saved_data_information.setObjectName(u"saved_data_information")
        self.saved_data_information.setGeometry(QRect(760, 10, 371, 131))
        self.saved_data_information.setFont(font)
        self.layoutWidget2 = QWidget(self.saved_data_information)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 20, 321, 101))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_name = QLabel(self.layoutWidget2)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_name)

        self.label_id = QLabel(self.layoutWidget2)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_id)

        self.label_date = QLabel(self.layoutWidget2)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_date)


        self.gridLayout_4.addLayout(self.verticalLayout_15, 0, 0, 1, 1)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.name_for_csv = QLineEdit(self.layoutWidget2)
        self.name_for_csv.setObjectName(u"name_for_csv")
        font3 = QFont()
        font3.setFamilies([u"Lato Thin"])
        font3.setPointSize(12)
        font3.setBold(False)
        self.name_for_csv.setFont(font3)

        self.verticalLayout_16.addWidget(self.name_for_csv)

        self.id_for_csv = QLineEdit(self.layoutWidget2)
        self.id_for_csv.setObjectName(u"id_for_csv")
        self.id_for_csv.setFont(font3)

        self.verticalLayout_16.addWidget(self.id_for_csv)

        self.date_for_csv = QDateEdit(self.layoutWidget2)
        self.date_for_csv.setObjectName(u"date_for_csv")
        self.date_for_csv.setFont(font3)
        self.date_for_csv.setCalendarPopup(True)
        self.date_for_csv.setDate(QDate.currentDate())

        self.verticalLayout_16.addWidget(self.date_for_csv)


        self.gridLayout_4.addLayout(self.verticalLayout_16, 0, 1, 1, 1)

        self.recordButton = QPushButton(self.data_management_widget)
        self.recordButton.setObjectName(u"recordButton")
        self.recordButton.setGeometry(QRect(1660, 20, 200, 120))
        self.recordButton.setMinimumSize(QSize(200, 120))
        font4 = QFont()
        font4.setFamilies([u"Lato"])
        font4.setPointSize(33)
        font4.setBold(True)
        self.recordButton.setFont(font4)
        self.recordButton.setStyleSheet(u"QPushButton{\n"
"	    background-color: rgb(74, 222, 128);\n"
"        border-style: solid;\n"
"        border-width: 2px;\n"
"        border-radius: 10px;  \n"
"        border-color: rgb(74, 222, 128);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"        border-color: #38bdf8;  /* Change border color on hover */\n"
"}")
        self.recordButton.setCheckable(False)
        self.recordButton.setAutoDefault(False)
        self.logoWTMH = QLabel(self.data_management_widget)
        self.logoWTMH.setObjectName(u"logoWTMH")
        self.logoWTMH.setGeometry(QRect(30, 10, 120, 120))
        self.logoWTMH.setMinimumSize(QSize(120, 120))
        self.logoWTMH.setPixmap(QPixmap(u":/images/images/WTMH.png"))
        self.logoWTMH.setScaledContents(True)

        self.gridLayout_5.addWidget(self.data_management_widget, 0, 0, 1, 1)

        self.data_visualization_widget = QWidget(self.centralwidget)
        self.data_visualization_widget.setObjectName(u"data_visualization_widget")
        self.data_visualization_widget.setMaximumSize(QSize(1871, 16777215))
        self.real_time_value = QGroupBox(self.data_visualization_widget)
        self.real_time_value.setObjectName(u"real_time_value")
        self.real_time_value.setGeometry(QRect(10, 10, 1360, 861))
        self.real_time_value.setMaximumSize(QSize(1360, 900))
        font5 = QFont()
        font5.setFamilies([u"Lato Heavy"])
        font5.setPointSize(12)
        self.real_time_value.setFont(font5)
        self.joint_static = QWidget(self.real_time_value)
        self.joint_static.setObjectName(u"joint_static")
        self.joint_static.setGeometry(QRect(10, 30, 661, 820))
        self.joint_static.setMaximumSize(QSize(680, 820))
        self.joint_static.setStyleSheet(u"")
        self.layoutWidget3 = QWidget(self.joint_static)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 1, 651, 811))
        self.verticalLayout_19 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.layoutWidget3)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(210, 30))
        font6 = QFont()
        font6.setFamilies([u"Lato Thin"])
        font6.setPointSize(18)
        font6.setBold(False)
        font6.setUnderline(True)
        self.label_25.setFont(font6)
        self.label_25.setStyleSheet(u"")

        self.verticalLayout_19.addWidget(self.label_25)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_11 = QLabel(self.layoutWidget3)
        self.label_11.setObjectName(u"label_11")
        font7 = QFont()
        font7.setFamilies([u"Lato"])
        font7.setPointSize(12)
        self.label_11.setFont(font7)

        self.verticalLayout.addWidget(self.label_11)

        self.metacarpal_table = QTableWidget(self.layoutWidget3)
        if (self.metacarpal_table.columnCount() < 3):
            self.metacarpal_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.metacarpal_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.metacarpal_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.metacarpal_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.metacarpal_table.rowCount() < 5):
            self.metacarpal_table.setRowCount(5)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.metacarpal_table.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.metacarpal_table.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.metacarpal_table.setVerticalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.metacarpal_table.setVerticalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.metacarpal_table.setVerticalHeaderItem(4, __qtablewidgetitem7)
        self.metacarpal_table.setObjectName(u"metacarpal_table")
        font8 = QFont()
        font8.setFamilies([u"Lato"])
        font8.setPointSize(9)
        self.metacarpal_table.setFont(font8)
        self.metacarpal_table.horizontalHeader().setMinimumSectionSize(32)
        self.metacarpal_table.horizontalHeader().setDefaultSectionSize(88)
        self.metacarpal_table.verticalHeader().setMinimumSectionSize(23)
        self.metacarpal_table.verticalHeader().setDefaultSectionSize(66)

        self.verticalLayout.addWidget(self.metacarpal_table)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_12 = QLabel(self.layoutWidget3)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font7)

        self.verticalLayout_2.addWidget(self.label_12)

        self.proximal_table = QTableWidget(self.layoutWidget3)
        if (self.proximal_table.columnCount() < 3):
            self.proximal_table.setColumnCount(3)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.proximal_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.proximal_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.proximal_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        if (self.proximal_table.rowCount() < 5):
            self.proximal_table.setRowCount(5)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.proximal_table.setVerticalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.proximal_table.setVerticalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.proximal_table.setVerticalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.proximal_table.setVerticalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.proximal_table.setVerticalHeaderItem(4, __qtablewidgetitem15)
        self.proximal_table.setObjectName(u"proximal_table")
        self.proximal_table.setFont(font8)
        self.proximal_table.horizontalHeader().setMinimumSectionSize(32)
        self.proximal_table.horizontalHeader().setDefaultSectionSize(88)
        self.proximal_table.verticalHeader().setMinimumSectionSize(23)
        self.proximal_table.verticalHeader().setDefaultSectionSize(66)

        self.verticalLayout_2.addWidget(self.proximal_table)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_13 = QLabel(self.layoutWidget3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font7)

        self.verticalLayout_3.addWidget(self.label_13)

        self.intermediate_table = QTableWidget(self.layoutWidget3)
        if (self.intermediate_table.columnCount() < 3):
            self.intermediate_table.setColumnCount(3)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.intermediate_table.setHorizontalHeaderItem(0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.intermediate_table.setHorizontalHeaderItem(1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.intermediate_table.setHorizontalHeaderItem(2, __qtablewidgetitem18)
        if (self.intermediate_table.rowCount() < 5):
            self.intermediate_table.setRowCount(5)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.intermediate_table.setVerticalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.intermediate_table.setVerticalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.intermediate_table.setVerticalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.intermediate_table.setVerticalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.intermediate_table.setVerticalHeaderItem(4, __qtablewidgetitem23)
        self.intermediate_table.setObjectName(u"intermediate_table")
        self.intermediate_table.setFont(font8)
        self.intermediate_table.horizontalHeader().setMinimumSectionSize(32)
        self.intermediate_table.horizontalHeader().setDefaultSectionSize(88)
        self.intermediate_table.verticalHeader().setMinimumSectionSize(23)
        self.intermediate_table.verticalHeader().setDefaultSectionSize(66)

        self.verticalLayout_3.addWidget(self.intermediate_table)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_14 = QLabel(self.layoutWidget3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font7)

        self.verticalLayout_4.addWidget(self.label_14)

        self.distal_table = QTableWidget(self.layoutWidget3)
        if (self.distal_table.columnCount() < 3):
            self.distal_table.setColumnCount(3)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.distal_table.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.distal_table.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.distal_table.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        if (self.distal_table.rowCount() < 5):
            self.distal_table.setRowCount(5)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.distal_table.setVerticalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.distal_table.setVerticalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.distal_table.setVerticalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.distal_table.setVerticalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.distal_table.setVerticalHeaderItem(4, __qtablewidgetitem31)
        self.distal_table.setObjectName(u"distal_table")
        self.distal_table.setFont(font8)
        self.distal_table.horizontalHeader().setMinimumSectionSize(32)
        self.distal_table.horizontalHeader().setDefaultSectionSize(88)
        self.distal_table.verticalHeader().setMinimumSectionSize(23)
        self.distal_table.verticalHeader().setDefaultSectionSize(66)

        self.verticalLayout_4.addWidget(self.distal_table)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 1, 1, 1, 1)


        self.verticalLayout_19.addLayout(self.gridLayout_2)

        self.angle_of_joint = QWidget(self.real_time_value)
        self.angle_of_joint.setObjectName(u"angle_of_joint")
        self.angle_of_joint.setGeometry(QRect(690, 30, 661, 820))
        self.angle_of_joint.setMaximumSize(QSize(680, 820))
        self.angle_of_joint.setStyleSheet(u"")
        self.layoutWidget4 = QWidget(self.angle_of_joint)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(10, 0, 641, 821))
        self.verticalLayout_18 = QVBoxLayout(self.layoutWidget4)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.layoutWidget4)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMaximumSize(QSize(320, 30))
        self.label_26.setFont(font6)
        self.label_26.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.label_26)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.metacarpal_widget = QWidget(self.layoutWidget4)
        self.metacarpal_widget.setObjectName(u"metacarpal_widget")
        self.metacarpal_widget.setMaximumSize(QSize(640, 180))
        self.metacarpal_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(244,221,182);\n"
"}")
        self.metacarpal_plot = QWidget(self.metacarpal_widget)
        self.metacarpal_plot.setObjectName(u"metacarpal_plot")
        self.metacarpal_plot.setGeometry(QRect(10, 10, 621, 161))

        self.verticalLayout_17.addWidget(self.metacarpal_widget)

        self.proximal_widget = QWidget(self.layoutWidget4)
        self.proximal_widget.setObjectName(u"proximal_widget")
        self.proximal_widget.setMaximumSize(QSize(640, 180))
        self.proximal_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(244,221,182);\n"
"}")
        self.proximal_plot = QWidget(self.proximal_widget)
        self.proximal_plot.setObjectName(u"proximal_plot")
        self.proximal_plot.setGeometry(QRect(10, 10, 621, 161))

        self.verticalLayout_17.addWidget(self.proximal_widget)

        self.intermediate_widget = QWidget(self.layoutWidget4)
        self.intermediate_widget.setObjectName(u"intermediate_widget")
        self.intermediate_widget.setMaximumSize(QSize(640, 180))
        self.intermediate_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(244,221,182);\n"
"}")
        self.intermediate_plot = QWidget(self.intermediate_widget)
        self.intermediate_plot.setObjectName(u"intermediate_plot")
        self.intermediate_plot.setGeometry(QRect(10, 10, 621, 161))

        self.verticalLayout_17.addWidget(self.intermediate_widget)

        self.distal_widget = QWidget(self.layoutWidget4)
        self.distal_widget.setObjectName(u"distal_widget")
        self.distal_widget.setMaximumSize(QSize(640, 180))
        self.distal_widget.setStyleSheet(u"QWidget{\n"
"	background-color:rgb(244,221,182);\n"
"}")
        self.distal_plot = QWidget(self.distal_widget)
        self.distal_plot.setObjectName(u"distal_plot")
        self.distal_plot.setGeometry(QRect(10, 10, 621, 161))

        self.verticalLayout_17.addWidget(self.distal_widget)


        self.verticalLayout_18.addLayout(self.verticalLayout_17)

        self.real_time_skeleton_view = QGroupBox(self.data_visualization_widget)
        self.real_time_skeleton_view.setObjectName(u"real_time_skeleton_view")
        self.real_time_skeleton_view.setGeometry(QRect(1380, 10, 481, 861))
        self.real_time_skeleton_view.setMaximumSize(QSize(501, 861))
        font9 = QFont()
        font9.setFamilies([u"Lato Heavy"])
        font9.setPointSize(12)
        font9.setBold(False)
        self.real_time_skeleton_view.setFont(font9)
        self.layoutWidget5 = QWidget(self.real_time_skeleton_view)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(10, 20, 461, 831))
        self.gridLayout = QGridLayout(self.layoutWidget5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.layoutWidget5)
        self.label.setObjectName(u"label")
        font10 = QFont()
        font10.setFamilies([u"Lato Thin"])
        font10.setPointSize(18)
        font10.setBold(False)
        self.label.setFont(font10)

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignHCenter)

        self.label_15 = QLabel(self.layoutWidget5)
        self.label_15.setObjectName(u"label_15")
        font11 = QFont()
        font11.setFamilies([u"Lato"])
        font11.setPointSize(9)
        font11.setBold(False)
        self.label_15.setFont(font11)
        self.label_15.setStyleSheet(u"QVBoxLayout{\n"
"	text-align:left;\n"
"}")
        self.label_15.setPixmap(QPixmap(u":/images/images/Screenshot 2024-03-27 173518.png"))
        self.label_15.setScaledContents(True)

        self.verticalLayout_5.addWidget(self.label_15)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_16 = QLabel(self.layoutWidget5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font10)

        self.verticalLayout_10.addWidget(self.label_16, 0, Qt.AlignHCenter)

        self.label_31 = QLabel(self.layoutWidget5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font1)
        self.label_31.setStyleSheet(u"QVBoxLayout{\n"
"	text-align:left;\n"
"}")
        self.label_31.setPixmap(QPixmap(u":/images/images/Screenshot 2024-03-27 173518.png"))
        self.label_31.setScaledContents(True)

        self.verticalLayout_10.addWidget(self.label_31)


        self.gridLayout.addLayout(self.verticalLayout_10, 1, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_32 = QLabel(self.layoutWidget5)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font10)

        self.verticalLayout_11.addWidget(self.label_32, 0, Qt.AlignHCenter)

        self.label_33 = QLabel(self.layoutWidget5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"QVBoxLayout{\n"
"	text-align:left;\n"
"}")
        self.label_33.setPixmap(QPixmap(u":/images/images/Screenshot 2024-03-27 173518.png"))
        self.label_33.setScaledContents(True)

        self.verticalLayout_11.addWidget(self.label_33)


        self.gridLayout.addLayout(self.verticalLayout_11, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.data_visualization_widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.data_logger.setTitle(QCoreApplication.translate("MainWindow", u"Enable Data Logger", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"New Data", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Overwrite", None))
        self.device_connection.setTitle(QCoreApplication.translate("MainWindow", u"Device Connection", None))
        self.device_top.setText(QCoreApplication.translate("MainWindow", u"Device Top:", None))
        self.device_bottom.setText(QCoreApplication.translate("MainWindow", u"Device Bottom:", None))
        self.device_side_2.setText(QCoreApplication.translate("MainWindow", u"Device Side:", None))
        self.device_top_status.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.device_bottom_status.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.device_side_status.setText(QCoreApplication.translate("MainWindow", u"Disconnected", None))
        self.saved_data_information.setTitle(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.recordButton.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.logoWTMH.setText("")
        self.real_time_value.setTitle(QCoreApplication.translate("MainWindow", u"Real Time Value", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Joint Static", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Metacarpal", None))
        ___qtablewidgetitem = self.metacarpal_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"D Top", None));
        ___qtablewidgetitem1 = self.metacarpal_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"D Bottom", None));
        ___qtablewidgetitem2 = self.metacarpal_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"D Side", None));
        ___qtablewidgetitem3 = self.metacarpal_table.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Thumb", None));
        ___qtablewidgetitem4 = self.metacarpal_table.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Index", None));
        ___qtablewidgetitem5 = self.metacarpal_table.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Middle", None));
        ___qtablewidgetitem6 = self.metacarpal_table.verticalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Ring", None));
        ___qtablewidgetitem7 = self.metacarpal_table.verticalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Pinky", None));
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Proximal", None))
        ___qtablewidgetitem8 = self.proximal_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"D Top", None));
        ___qtablewidgetitem9 = self.proximal_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"D Bottom", None));
        ___qtablewidgetitem10 = self.proximal_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"D Side", None));
        ___qtablewidgetitem11 = self.proximal_table.verticalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Thumb", None));
        ___qtablewidgetitem12 = self.proximal_table.verticalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Index", None));
        ___qtablewidgetitem13 = self.proximal_table.verticalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Middle", None));
        ___qtablewidgetitem14 = self.proximal_table.verticalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Ring", None));
        ___qtablewidgetitem15 = self.proximal_table.verticalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Pinky", None));
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Intermediate", None))
        ___qtablewidgetitem16 = self.intermediate_table.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"D Top", None));
        ___qtablewidgetitem17 = self.intermediate_table.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"D Bottom", None));
        ___qtablewidgetitem18 = self.intermediate_table.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"D Side", None));
        ___qtablewidgetitem19 = self.intermediate_table.verticalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Thumb", None));
        ___qtablewidgetitem20 = self.intermediate_table.verticalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Index", None));
        ___qtablewidgetitem21 = self.intermediate_table.verticalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Middle", None));
        ___qtablewidgetitem22 = self.intermediate_table.verticalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Ring", None));
        ___qtablewidgetitem23 = self.intermediate_table.verticalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Pinky", None));
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Distal", None))
        ___qtablewidgetitem24 = self.distal_table.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"D Top", None));
        ___qtablewidgetitem25 = self.distal_table.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"D Bottom", None));
        ___qtablewidgetitem26 = self.distal_table.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"D Side", None));
        ___qtablewidgetitem27 = self.distal_table.verticalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Thumb", None));
        ___qtablewidgetitem28 = self.distal_table.verticalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Index", None));
        ___qtablewidgetitem29 = self.distal_table.verticalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Middle", None));
        ___qtablewidgetitem30 = self.distal_table.verticalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Ring", None));
        ___qtablewidgetitem31 = self.distal_table.verticalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Pinky", None));
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Angle of Joints Plot", None))
        self.real_time_skeleton_view.setTitle(QCoreApplication.translate("MainWindow", u"Real Time Skeleton View", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Top View", None))
        self.label_15.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Bottom View", None))
        self.label_31.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Side View", None))
        self.label_33.setText("")
    # retranslateUi

