# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_AirConditioner.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 600)
        Form.setMinimumSize(QtCore.QSize(1200, 600))
        Form.setMaximumSize(QtCore.QSize(1200, 600))
        Form.setStyleSheet("")
        self.widget_1 = QtWidgets.QWidget(Form)
        self.widget_1.setGeometry(QtCore.QRect(0, 0, 1200, 600))
        self.widget_1.setStyleSheet("#widget_1{\n"
"background-color: #40bad5;\n"
"border-radius: 10px;\n"
"}\n"
"#widget_2{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"QStackedWidget{\n"
"border-color: rgb(0, 0, 0);\n"
"background-color:#40bad5;\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 15;\n"
"\n"
"}\n"
"QWidget{\n"
"\n"
"}\n"
"#page_control, #page_instruction{\n"
"background-color:#40bad5;\n"
"}\n"
"QPushButton {\n"
"font: 12pt \"黑体\";\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: #035aa6;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding: 8;\n"
"}\n"
"QPushButton:hover{\n"
"border-color: rgb(0, 0, 0);\n"
"background-color:#fcf876;\n"
"color:  rgb(123, 139, 111);\n"
"border-radius: 10px;\n"
"padding: 8;\n"
"}\n"
"QPushButton:active{\n"
"position:relative;\n"
"top:1px;\n"
"}\n"
"QLabel{\n"
"font: 16pt \"黑体\";\n"
"border-color: rgb(0, 0, 0);\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"}\n"
"QLCDNumber{\n"
"color:rgb(255, 255, 127);\n"
"background-color: #120136;\n"
"border-radius: 10px;\n"
"}\n"
"Line{\n"
"background-color: #40bad5;\n"
"border-radius: 5px;\n"
"}\n"
"QTextBrowser{\n"
"font: 14pt \"黑体\";\n"
"color: rgb(0, 0, 0);\n"
"border-radius: 10px;\n"
"padding: 8;\n"
"background:transparent;\n"
"}")
        self.widget_1.setObjectName("widget_1")
        self.widget_2 = QtWidgets.QWidget(self.widget_1)
        self.widget_2.setGeometry(QtCore.QRect(40, 40, 1121, 521))
        self.widget_2.setObjectName("widget_2")
        self.pushButton_instruction = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_instruction.setGeometry(QtCore.QRect(900, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_instruction.setFont(font)
        self.pushButton_instruction.setStyleSheet("")
        self.pushButton_instruction.setObjectName("pushButton_instruction")
        self.pushButton_sub_temperature = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_sub_temperature.setGeometry(QtCore.QRect(730, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sub_temperature.setFont(font)
        self.pushButton_sub_temperature.setObjectName("pushButton_sub_temperature")
        self.pushButton_sub_wind = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_sub_wind.setGeometry(QtCore.QRect(560, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_sub_wind.setFont(font)
        self.pushButton_sub_wind.setObjectName("pushButton_sub_wind")
        self.lcdNumber_temperature_target = QtWidgets.QLCDNumber(self.widget_2)
        self.lcdNumber_temperature_target.setGeometry(QtCore.QRect(730, 100, 111, 71))
        self.lcdNumber_temperature_target.setStyleSheet("color: rgb(255, 0, 0);")
        self.lcdNumber_temperature_target.setDigitCount(4)
        self.lcdNumber_temperature_target.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_temperature_target.setObjectName("lcdNumber_temperature_target")
        self.pushButton_exit = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_exit.setGeometry(QtCore.QRect(900, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_exit.setFont(font)
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label_show_temperature_current = QtWidgets.QLabel(self.widget_2)
        self.label_show_temperature_current.setGeometry(QtCore.QRect(570, 40, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_show_temperature_current.setFont(font)
        self.label_show_temperature_current.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_temperature_current.setObjectName("label_show_temperature_current")
        self.pushButton_ON_OFF = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_ON_OFF.setGeometry(QtCore.QRect(900, 60, 141, 101))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_ON_OFF.setFont(font)
        self.pushButton_ON_OFF.setStyleSheet("")
        self.pushButton_ON_OFF.setObjectName("pushButton_ON_OFF")
        self.pushButton_add_temperature = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_add_temperature.setGeometry(QtCore.QRect(730, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_add_temperature.setFont(font)
        self.pushButton_add_temperature.setObjectName("pushButton_add_temperature")
        self.pushButton_add_wind = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_add_wind.setGeometry(QtCore.QRect(560, 200, 141, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_add_wind.setFont(font)
        self.pushButton_add_wind.setObjectName("pushButton_add_wind")
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_2)
        self.stackedWidget.setGeometry(QtCore.QRect(80, 40, 461, 271))
        self.stackedWidget.setStyleSheet("")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_control = QtWidgets.QWidget()
        self.page_control.setStyleSheet("")
        self.page_control.setObjectName("page_control")
        self.label_show_RoomId = QtWidgets.QLabel(self.page_control)
        self.label_show_RoomId.setGeometry(QtCore.QRect(40, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_show_RoomId.setFont(font)
        self.label_show_RoomId.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_RoomId.setObjectName("label_show_RoomId")
        self.label_speed_wind = QtWidgets.QLabel(self.page_control)
        self.label_speed_wind.setGeometry(QtCore.QRect(230, 110, 171, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_speed_wind.setFont(font)
        self.label_speed_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed_wind.setObjectName("label_speed_wind")
        self.label_fee_current = QtWidgets.QLabel(self.page_control)
        self.label_fee_current.setGeometry(QtCore.QRect(250, 160, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_fee_current.setFont(font)
        self.label_fee_current.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fee_current.setObjectName("label_fee_current")
        self.label_RoomId = QtWidgets.QLabel(self.page_control)
        self.label_RoomId.setGeometry(QtCore.QRect(230, 10, 171, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_RoomId.setFont(font)
        self.label_RoomId.setAlignment(QtCore.Qt.AlignCenter)
        self.label_RoomId.setObjectName("label_RoomId")
        self.label_mode = QtWidgets.QLabel(self.page_control)
        self.label_mode.setGeometry(QtCore.QRect(230, 60, 171, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_mode.setFont(font)
        self.label_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_mode.setObjectName("label_mode")
        self.label_show_fee_current = QtWidgets.QLabel(self.page_control)
        self.label_show_fee_current.setGeometry(QtCore.QRect(40, 160, 151, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_show_fee_current.setFont(font)
        self.label_show_fee_current.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_fee_current.setObjectName("label_show_fee_current")
        self.label_show_mode = QtWidgets.QLabel(self.page_control)
        self.label_show_mode.setGeometry(QtCore.QRect(40, 60, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_show_mode.setFont(font)
        self.label_show_mode.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_mode.setObjectName("label_show_mode")
        self.label_show_speed_wind = QtWidgets.QLabel(self.page_control)
        self.label_show_speed_wind.setGeometry(QtCore.QRect(40, 110, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_show_speed_wind.setFont(font)
        self.label_show_speed_wind.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_speed_wind.setObjectName("label_show_speed_wind")
        self.label_fee_total = QtWidgets.QLabel(self.page_control)
        self.label_fee_total.setGeometry(QtCore.QRect(250, 210, 131, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_fee_total.setFont(font)
        self.label_fee_total.setAlignment(QtCore.Qt.AlignCenter)
        self.label_fee_total.setObjectName("label_fee_total")
        self.label_show_fee_total = QtWidgets.QLabel(self.page_control)
        self.label_show_fee_total.setGeometry(QtCore.QRect(40, 210, 151, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_show_fee_total.setFont(font)
        self.label_show_fee_total.setAlignment(QtCore.Qt.AlignCenter)
        self.label_show_fee_total.setObjectName("label_show_fee_total")
        self.stackedWidget.addWidget(self.page_control)
        self.page_instruction = QtWidgets.QWidget()
        self.page_instruction.setStyleSheet("")
        self.page_instruction.setObjectName("page_instruction")
        self.textBrowser_instruction = QtWidgets.QTextBrowser(self.page_instruction)
        self.textBrowser_instruction.setGeometry(QtCore.QRect(0, 10, 441, 221))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.textBrowser_instruction.setFont(font)
        self.textBrowser_instruction.setObjectName("textBrowser_instruction")
        self.pushButton_instruction_back = QtWidgets.QPushButton(self.page_instruction)
        self.pushButton_instruction_back.setGeometry(QtCore.QRect(310, 200, 101, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton_instruction_back.setFont(font)
        self.pushButton_instruction_back.setObjectName("pushButton_instruction_back")
        self.stackedWidget.addWidget(self.page_instruction)
        self.label_temperature_target = QtWidgets.QLabel(self.widget_2)
        self.label_temperature_target.setGeometry(QtCore.QRect(730, 40, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_temperature_target.setFont(font)
        self.label_temperature_target.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temperature_target.setObjectName("label_temperature_target")
        self.lcdNumber_temperature_current = QtWidgets.QLCDNumber(self.widget_2)
        self.lcdNumber_temperature_current.setGeometry(QtCore.QRect(580, 100, 111, 71))
        self.lcdNumber_temperature_current.setDigitCount(4)
        self.lcdNumber_temperature_current.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcdNumber_temperature_current.setObjectName("lcdNumber_temperature_current")
        self.label_1 = QtWidgets.QLabel(self.widget_2)
        self.label_1.setGeometry(QtCore.QRect(80, 360, 971, 30))
        self.label_1.setStyleSheet("background-color: #f4a548;")
        self.label_1.setText("")
        self.label_1.setObjectName("label_1")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(80, 410, 971, 30))
        self.label_2.setStyleSheet("background-color: #f4a548;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(80, 460, 971, 30))
        self.label_3.setStyleSheet("background-color: rgb(0, 200, 255);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_exit.clicked.connect(Form.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_instruction.setText(_translate("Form", "使用说明"))
        self.pushButton_sub_temperature.setText(_translate("Form", "温度-"))
        self.pushButton_sub_wind.setText(_translate("Form", "风速-"))
        self.pushButton_exit.setText(_translate("Form", "退出"))
        self.label_show_temperature_current.setText(_translate("Form", "当前室温"))
        self.pushButton_ON_OFF.setText(_translate("Form", "开关"))
        self.pushButton_add_temperature.setText(_translate("Form", "温度+"))
        self.pushButton_add_wind.setText(_translate("Form", "风速+"))
        self.label_show_RoomId.setText(_translate("Form", "房间号"))
        self.label_speed_wind.setText(_translate("Form", "低/中/高速"))
        self.label_fee_current.setText(_translate("Form", "10.2"))
        self.label_RoomId.setText(_translate("Form", "12138"))
        self.label_mode.setText(_translate("Form", "制冷/制热"))
        self.label_show_fee_current.setText(_translate("Form", "当前费用/元"))
        self.label_show_mode.setText(_translate("Form", "工作模式"))
        self.label_show_speed_wind.setText(_translate("Form", "风速"))
        self.label_fee_total.setText(_translate("Form", "100.2"))
        self.label_show_fee_total.setText(_translate("Form", "累计费用/元"))
        self.textBrowser_instruction.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'黑体\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'华文仿宋\'; font-size:16pt;\">这里是使用方法+计费规则123ABC</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'华文仿宋\'; font-size:16pt;\"><br /></p></body></html>"))
        self.pushButton_instruction_back.setText(_translate("Form", "返回"))
        self.label_temperature_target.setText(_translate("Form", "目标温度"))
