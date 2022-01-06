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


# import GetSimilarity as GetAns

if __name__ == "__main__":
    # while(True):
    #     text = input()
    #     print(GetAns.getAns(text))

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(window)
    ui.changeMovie("smile")

    number = dt.hello()
    if (number > 0):
        ui.onlyAnswer("检测到" + str(number) + "个人。您好！请问您叫什么名字？")
        ui.changeMovie("hello")
    else:
        ui.onlyAnswer("请问这里有人吗!")
        ui.changeMovie("question")
    #默认状态
    window.show()

    sys.exit(app.exec_())
