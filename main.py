from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import requests
from requests import ConnectionError, ReadTimeout
import threading
import time
import GUI_AirConditioner
import MyMainWindow


class AirConditioner:
    dict_mode = {0: '制冷', 1: '制热'}
    dict_wind = {1: '低', 2: '中', 3: '高'}

    def __init__(self, room, current):
        self.__init_temper = current  # 初始温度
        self.__room = room  # 房间号
        self.__power = False  # 空调是否打开
        self.__mode = 0  # 制冷制热
        self.__target = 25.0  # 目标温度
        self.__current = current  # 当前温度
        self.__wind = 2  # 风力等级
        self.__cost = ""  # 花费

        self.__GUI = GUI_AirConditioner.Ui_Form()
        app = QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.__GUI.setupUi(MainWindow)
        MainWindow.show()
        self.__GUI.label_RoomId.setText(self.__room)
        self.__GUI.pushButton_ON_OFF.setText("开机")
        self.__GUI.label_mode.setText(self.dict_mode[self.__mode])
        self.__GUI.lcdNumber_temperature_current.display(str(round(self.__current, 1)))
        self.__GUI.lcdNumber_temperature_target.display(str(round(self.__target, 1)))
        self.__GUI.label_speed_wind.setText(self.dict_wind[self.__wind])
        self.__GUI.label_fee_current.setText(str(0))
        self.__GUI.label_fee_total.setText(self.__cost)
        self.__GUI.pushButton_ON_OFF.clicked.connect(self.on_pushButton_ON_OFF_clicked)
        self.__GUI.pushButton_instruction.clicked.connect(self.on_pushButton_instruction_clicked)
        self.__GUI.pushButton_add_temperature.clicked.connect(self.on_pushButton_add_temperature_clicked)
        self.__GUI.pushButton_sub_temperature.clicked.connect(self.on_pushButton_sub_temperature_clicked)
        self.__GUI.pushButton_add_wind.clicked.connect(self.on_pushButton_add_wind_clicked)
        self.__GUI.pushButton_sub_wind.clicked.connect(self.on_pushButton_sub_wind_clicked)
        self.__GUI.pushButton_instruction_back.clicked.connect(self.on_pushButton_instruction_back_clicked)
        self.__GUI.pushButton_exit.clicked.connect(self.on_pushButton_exit_clicked)
        self.__GUI.pushButton_ON_OFF.setEnabled(True)
        self.__GUI.pushButton_instruction.setEnabled(True)
        self.__GUI.pushButton_add_temperature.setEnabled(False)
        self.__GUI.pushButton_sub_temperature.setEnabled(False)
        self.__GUI.pushButton_add_wind.setEnabled(False)
        self.__GUI.pushButton_sub_wind.setEnabled(False)
        self.__GUI.pushButton_instruction.setEnabled(True)
        app.exec_()
        if self.__power:
            self.set_power(False)

    def on_pushButton_ON_OFF_clicked(self):
        self.set_power(not self.get_power())
        if self.__power:
            self.__GUI.pushButton_ON_OFF.setText("关机")
            self.__GUI.pushButton_add_temperature.setEnabled(True)
            self.__GUI.pushButton_add_temperature.setStyleSheet("background-color: #035aa6;QPushButton:hover{"
                                                                "background-color:#fcf876;}")
            self.__GUI.pushButton_sub_temperature.setEnabled(True)
            self.__GUI.pushButton_sub_temperature.setStyleSheet("background-color: #035aa6;QPushButton:hover{"
                                                                "background-color:#fcf876;}")
            self.__GUI.pushButton_add_wind.setEnabled(True)
            self.__GUI.pushButton_add_wind.setStyleSheet("background-color: #035aa6;QPushButton:hover{"
                                                         "background-color:#fcf876;}")
            self.__GUI.pushButton_sub_wind.setEnabled(True)
            self.__GUI.pushButton_sub_wind.setStyleSheet("background-color: #035aa6;QPushButton:hover{background"
                                                         "-color:#fcf876;}")


        else:
            self.__GUI.pushButton_ON_OFF.setText("开机")
            self.__GUI.pushButton_add_temperature.setStyleSheet("background-color: #43d8c9;")
            self.__GUI.pushButton_add_temperature.setEnabled(False)
            self.__GUI.pushButton_sub_temperature.setStyleSheet("background-color: #43d8c9;")
            self.__GUI.pushButton_sub_temperature.setEnabled(False)
            self.__GUI.pushButton_add_wind.setStyleSheet("background-color: #43d8c9;")
            self.__GUI.pushButton_add_wind.setEnabled(False)
            self.__GUI.pushButton_sub_wind.setStyleSheet("background-color: #43d8c9;")
            self.__GUI.pushButton_sub_wind.setEnabled(False)
            # QtWidgets.QApplication.processEvents()  # 界面实时刷新

    def on_pushButton_instruction_clicked(self):
        self.__GUI.stackedWidget.setCurrentIndex(1)
        #  TODO 展示使用方法+计费规则
        str_use = "【使用方法】\n"
        str_use += "点击”开机“键进行开机，开机后可以关机、调节温度、调节风速\n"
        str_use += "点击”使用说明“即可查看使用方法和计费规则\n"
        str_use += "点击”温度+“（或“温度-”）即可提高（或降低）目标温度0.5°C\n"
        str_use += "点击”风速+“（或“风速-”）即可提高（或降低）风速等级1级\n"
        str_rules = "【计费规则】\n"
        str_rules += "温控范围：制冷（16-24°C）（5月-9月）、制热（22-28°C）（11月-次年3月）\n"
        str_rules += "风速范围：低速风（0.5元/1°C）、中速风（1元/1°C）、高速风（2元/1°C）\n"
        str_rules += "默认值：20°C 低速风"
        self.__GUI.textBrowser_instruction.setText(str_use + "\n\n" + str_rules)
        pass

    def on_pushButton_add_temperature_clicked(self):
        if (0 == self.__mode and 16 <= self.__target < 24) or (1 == self.__mode and 22 <= self.__target < 28):
            self.__target += 0.5
        self.__GUI.lcdNumber_temperature_target.display(str(round(self.__target, 1)))

    def on_pushButton_sub_temperature_clicked(self):
        if (0 == self.__mode and 16 < self.__target <= 24) or (1 == self.__mode and 22 < self.__target <= 28):
            self.__target -= 0.5
        self.__GUI.lcdNumber_temperature_target.display(str(round(self.__target, 1)))

    def on_pushButton_add_wind_clicked(self):
        if 1 <= self.__wind < 3:
            self.__wind += 1
        self.__GUI.label_speed_wind.setText(self.dict_wind[self.__wind])

    def on_pushButton_sub_wind_clicked(self):
        if 1 < self.__wind <= 3:
            self.__wind -= 1
        self.__GUI.label_speed_wind.setText(self.dict_wind[self.__wind])

    def on_pushButton_instruction_back_clicked(self):
        self.__GUI.stackedWidget.setCurrentIndex(0)



    # 发送心跳包
    def heart_post(self):
        while self.__power:  # 仅在开机状态发送
            # 构造心跳包
            heart = {
                'room': self.__room,
                'power': self.__power,
                'mode': self.__mode,
                'target': self.__target,
                'current': round(self.__current, 3),
                'wind': self.__wind
            }
            print('')
            print("当前温度为:%s" % self.__current)
            print("发送的心跳包为")
            print(heart)
            try:
                r = requests.post("http://name1e5s.fun:3000/api/heartbeat", json=heart)
            except (ConnectionError, ReadTimeout):
                print('发送心跳包出现异常')
            else:
                result = r.json()
                print(result)
                self.__cost = result['cost']  # 更新面板金额
                if result['wind']:  # 服务器同意送风
                    if self.__mode == 0:  # 制冷模式
                        self.__current = self.__current - self.fee(self.__wind)

                    elif self.__mode == 1:  # 制热模式
                        self.__current = self.__current + self.fee(self.__wind)
                else:
                    print("空调不同意送风，进行回温")
                    if self.__mode == 0:  # 制冷向上回温
                        self.__current = self.__current + 0.25
                    else:
                        self.__current = self.__current - 0.25
                print('预计30s后温度可以达到 %s' % self.get_current())
                time.sleep(30)
                self.__GUI.lcdNumber_temperature_current.display(str(round(self.__current, 1)))
                self.__GUI.label_fee_current.setText(str(0))
                self.__GUI.label_fee_total.setText(str(round(self.__cost, 2)))

    # 开机发送注册包
    def register_post(self):
        # 构造post的json包
        register = {
            'room': self.__room
        }
        try:
            r = requests.post("http://name1e5s.fun:3000/api/register", json=register)
        except (ConnectionError, ReadTimeout):
            print('发送注册数据包出现问题')
            return
        print(r.text)

    # 温度变化标准
    def fee(self, w):
        if w == 1:
            return 1 / 6
        elif w == 2:
            return 1 / 4
        else:
            return 1 / 2

    def set_power(self, power):
        self.__power = power
        if power:  # 开机
            self.register_post()
            # 创建线程发送心跳包
            t_heartbeat = threading.Thread(target=self.heart_post, name='T_heart')
            t_heartbeat.start()
        else:  # 关机,温度回到初始温度
            self.set_current(self.__init_temper)

    def get_power(self):
        return self.__power

    def set_mode(self, mode):
        self.__power = mode

    def get_mode(self):
        return self.__mode

    def set_target(self, target):
        self.__power = target

    def get_target(self):
        return self.__target

    def set_wind(self, wind):
        self.__power = wind

    def get_wind(self):
        return self.__wind

    def get_current(self):
        return self.__current

    def set_current(self, temper):
        self.__current = temper

    def get_room(self):
        return self.__room

    def on_pushButton_exit_clicked(self):
        self.set_power(False)
        print("关闭程序")


roomid = input('请输入房间号')
temper = input('请输入当前温度')
# 创建空调对象
air = AirConditioner(roomid, float(temper))
