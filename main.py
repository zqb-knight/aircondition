from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
import requests
from requests import ConnectionError, ReadTimeout
import threading
import time
import GUI_AirConditioner


class AirConditioner:
    dict_mode = {0: '制冷', 1: '制热'}
    dict_wind = {1: '低', 2: '中', 3: '高'}

    def __init__(self, room, current):
        self.__room = room  # 房间号
        self.__power = False  # 空调是否打开
        self.__mode = 0  # 制冷制热
        self.__target = 23.0  # 目标温度
        self.__current = current  # 当前温度
        self.__wind = 1  # 风力等级
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
        self.__power = not self.__power
        if self.__power:
            self.__GUI.pushButton_ON_OFF.setText("关机")
            self.__GUI.pushButton_add_temperature.setEnabled(True)
            self.__GUI.pushButton_sub_temperature.setEnabled(True)
            self.__GUI.pushButton_add_wind.setEnabled(True)
            self.__GUI.pushButton_sub_wind.setEnabled(True)
            # 开机注册
            self.set_power(True)
            # 创建线程发送心跳包
            t_heartbeat = threading.Thread(target=self.heart_post, name='T_heart')
            # 创建线程模拟空调工作
            # t_work = threading.Thread(target=air.work, name='workT')
            # t_work.start()
            t_heartbeat.start()
            print('thread %s.' % threading.current_thread().name)
        else:
            self.__GUI.pushButton_ON_OFF.setText("开机")
            self.__GUI.pushButton_add_temperature.setEnabled(False)
            self.__GUI.pushButton_sub_temperature.setEnabled(False)
            self.__GUI.pushButton_add_wind.setEnabled(False)
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

    def closeEvent(self, event):
        self.set_power(False)
        print("重写成功")

    # 模拟空调工作过程
    def work(self):
        while True:
            if self.__power:  # 空调开机
                if self.__mode == 0:  # 制冷模式
                    if self.__target < self.__current:  # 未达到目标温度
                        self.__current = self.__current - self.__wind * 0.1
                    else:
                        self.set_power(False)  # 关机
                elif self.__mode == 1:  # 制热模式
                    if self.__target > self.__current:  # 未达到目标温度
                        self.__current = self.__current + self.__wind * 0.1
                    else:
                        self.set_power(False)  # 关机
            else:
                print("空调已关机")

            time.sleep(1)
            print('当前温度为 %s.' % self.__current)

    # 发送心跳包
    def heart_post(self):
        while self.__power:
            # 构造心跳包
            heart = {
                'room': self.__room,
                'power': self.__power,
                'mode': self.__mode,
                'target': self.__target,
                'current': self.__current,
                'wind': self.__wind
            }
            print("发送的心跳包为")
            print(heart)
            try:
                r = requests.post("http://localhost:8080/api/heartbeat", json=heart)
            except (ConnectionError, ReadTimeout):
                print('发送心跳包出现异常')
            else:
                result = r.json()
                # print(result['status'])
                print(result)
                if result['status'] == 0:  # STATUS_ACK
                    self.__cost = result['cost']  # 更新面板金额
                    if result['wind']:  # 服务器同意送风
                        if self.__mode == 0:  # 制冷模式
                            self.__current = self.__current - self.__wind * 0.1
                            print("当前温度为:%s" % self.__current)
                        elif self.__mode == 1:  # 制热模式
                            self.__current = self.__current + self.__wind * 0.1
                    else:
                        print("空调不同意送风")
                    self.__GUI.lcdNumber_temperature_current.display(str(round(self.__current, 1)))
                    self.__GUI.label_fee_current.setText(str(0))
                    self.__GUI.label_fee_total.setText(str(self.__cost))

                elif result['status'] == 1:  # STATUS_RST
                    print("重置空调状态")
                    __power = False  # 重置空调状态
                    __mode = 0
                    __target = 20.0
                    __current = 25.0
                    __wind = 1
                    __cost = "0"
                else:
                    print("出错")
            time.sleep(2)

    # 开机发送注册包
    def register_post(self):
        # 构造post的json包
        register = {
            'room': self.__room
        }
        try:
            r = requests.post("http://localhost:8080/api/register", json=register)
        except (ConnectionError, ReadTimeout):
            print('发送注册数据包出现问题')
            return
        print(r.text)

    def set_power(self, power):
        if power:  # 开机
            self.register_post()
        self.__power = power

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

    def get_room(self):
        return self.__room


# 创建空调对象
air = AirConditioner('211308', 24.8)
