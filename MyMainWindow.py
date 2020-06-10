from PyQt5 import Qt, QtGui
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMainWindow
import os


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.m_flag = False
        self.m_Position = 0
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.Qt.ArrowCursor))

    def closeEvent(self, event):
        event.accept()
        try:
            os._exit(5)
        except Exception as e:
            print(e)