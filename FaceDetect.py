# 检测视频人脸 ========================================================================

import os
from win32com.client import Dispatch
import cv2 as cv

print(os.getcwd())  # 获得当前目录
print('================================= 人脸识别程序 ==============================')

print('正在打开摄像头...')
print('加载人脸特征数据...')
def hello():
    cap = cv.VideoCapture(0)  # 调用自己的摄像头
    ret, frame = cap.read()
    if not ret:
        cap = cv.VideoCapture(1)
        ret, frame = cap.read()
        if not ret:
            print('未发现电脑摄像头，或未能打开摄像头，将进行本地视频人脸识别')  # False
            cap = cv.VideoCapture('video.mkv')
            ret, frame = cap.read()
            if not ret:
                quit()

    flag, frame = cap.read()
    speaker = Dispatch('SAPI.SpVoice')
    if flag:
        speaker.Speak("已打开摄像头")
    else:
        speaker.Speak("啊哦你的摄像头没打开")

    # 将视频帧的大小调整为1/2以加快人脸识别处理

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    face_detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_detector.detectMultiScale(gray)
    for (x, y, w, h) in faces:
        # 在原图上绘制矩形
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv.imshow('frame', frame)

    # cv.destroyAllWindows()  # 释放内存
    return len(faces)
    #if ord('q') == cv.waitKey(10):
        #break


