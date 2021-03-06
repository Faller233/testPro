# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import _thread
import random

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtGui import QMovie
from win32com.client import Dispatch

import Sound2Text as st
import QA as qa


#异步消息录音
class Mythread(QThread):
    # 定义信号,定义参数为str类型
    breakSignal = pyqtSignal(str)
    def __init__(self):
        super(Mythread, self).__init__()
    def __del__(self):
        self.wait()
    def run(self):
        words = st.func()
        self.breakSignal.emit(words)

class Ui_Dialog(object):
    random.seed()
    pics = ['hello','happy','NoAns']

    speaker = Dispatch('SAPI.SpVoice')
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(80, 250, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 250, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 60, 131, 131))
        self.label.setObjectName("label")
        self.userWords = QtWidgets.QTextEdit(Dialog)
        self.userWords.setGeometry(QtCore.QRect(240, 150, 150, 80))
        self.userWords.setObjectName("userWords")
        self.botWords = QtWidgets.QTextEdit(Dialog)
        self.botWords.setGeometry(QtCore.QRect(240, 50, 150, 80))
        self.botWords.setObjectName("botWords")

        self.pushButton.clicked.connect(self.dealWords)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "北理宝-您的第一款语音智障助手"))
        self.pushButton.setText(_translate("Dialog", "开始录音"))
        self.pushButton_2.setText(_translate("Dialog", "重新捕获"))
        self.label.setText(_translate("Dialog", "TextLabel"))

    # 要用self.thread表示当前实例的内容 此处开始录音
    def dealWords(self):
        self.thread = Mythread()
        # 注册信号处理函数
        self.pushButton.setEnabled(False)
        self.thread.breakSignal.connect(self.showMsg)
        # self.thread.setDaemon(True)
        self.changeMovie("hello")
        self.thread.start()

    # 切换虚拟形象图片
    def changeMovie(self, Words):
        if Words in self.pics:
            self.movie = QMovie("pics/" + Words + str(random.randint(1,4))+ ".gif")
        else:
            self.movie = QMovie("pics/NoAns" + str(random.randint(1,4)) + ".gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        # 显示用户说话内容 获得回答之后回显

    def onlyAnswer(self,answer):
        self.botWords.setText(answer)
        _thread.start_new_thread(self.speaker.speak, (answer,))

    def showMsg(self, Msg):
        # 用户说话
        self.userWords.setText(Msg)
        # 回答
        answer = qa.Turing(Msg)

        # 根据回答显示表情包
        if Msg == "啊咧，小助手不知道这个问题呢":
            self.changeMovie("NoAns")
        else:
            self.changeMovie("happy")

        self.botWords.setText(answer)
        _thread.start_new_thread(self.speaker.speak, (answer,))
        # 允许再次录音
        self.pushButton.setEnabled(True)
