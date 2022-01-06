import json
from collections import abc

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QIcon
import sys

from PyQt5.QtWidgets import QPushButton
import FaceDetect as dt
from MainUI import Ui_Dialog
import threading, time

# MyThread.py线程类
# class MyThread(threading.Thread):
#     def __init__(self, func, args=()):
#         super(MyThread, self).__init__()
#         self.func = func
#         self.args = args
#
#     def run(self):
#         time.sleep(2)
#         self.result = self.func(*self.args)
#
#     def get_result(self):
#         threading.Thread.join(self)  # 等待线程执行完毕
#         try:
#             return self.result
#         except Exception:
#             return None

if __name__ == "__main__":
    # print(233)
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(window)
    ui.changeMovie("smile")

    number = dt.hello()
    if (number > 0):
        ui.showMsg("检测到" + str(number) + "个人,您好，请问你需要什么帮助吗")
        ui.changeMovie("hello")
    else:
        ui.showMsg("没人吗这里？")
        ui.changeMovie("question")
    #默认状态
    window.show()


    sys.exit(app.exec_())
