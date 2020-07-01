from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import pickle
import time
import cv2
import os
import tkinter as tk
import threading

def recognize_video():   
    ## 创建识别窗口
    win_rec = tk.Tk()
    win_rec.title('人脸识别')
    win_rec.geometry('300x320')
    var_name = tk.StringVar()        
    var_proba = tk.StringVar()
    var_ans = tk.StringVar()
    
    ## 创建画布用于切换图片   
    canvas1 = tk.Canvas(win_rec, height = 129, width = 183)
    canvas2 = tk.Canvas(win_rec, height = 129, width = 183)
    stop = tk.PhotoImage(file = 'stop.gif')
    welcome = tk.PhotoImage(file = 'welcome.gif')
    canvas1.create_image(0,0, anchor = 'nw', image = stop)
    canvas2.create_image(0,0, anchor = 'nw', image = welcome)
    
    ## 创建Label用于显示人名及匹配度
    tk.Label(win_rec, text = '姓  名:').place(x = 50, y = 50)
    tk.Label(win_rec, text = '匹配度:').place(x = 50, y = 90)
    tk.Label(win_rec, textvariable = var_name).place(x = 100, y = 50)
    tk.Label(win_rec, textvariable = var_proba).place(x = 100, y = 90)
    tk.Label(win_rec, textvariable = var_ans).place(x = 100, y = 130)
    tk.Label(win_rec, text = '人脸识别系统v6').place(x=175, y=300)
    

print("[INFO] starting video stream...")
import cv2
import numpy as np

# 加载视频
cap = cv2.VideoCapture('4.mp4')

# 调用熟悉的人脸分类器 识别特征类型
# 人脸 - haarcascade_frontalface_default.xml
# 人眼 - haarcascade_eye.xm
# 微笑 - haarcascade_smile.xml
# face_detect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:
    # 读取视频片段
    flag, frame = cap.read()
    if flag == False:
        break

    # 灰度处理
    # gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)

    # 检查人脸 按照1.1倍放到 周围最小像素为5
    # face_zone = face_detect.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 4)

    # # 绘制矩形和圆形检测人脸
    # for x, y, w, h in face_zone:
    #     cv2.rectangle(frame, pt1 = (x, y), pt2 = (x+w, y+h), color = [0,0,255], thickness=2)
    #     cv2.circle(frame, center = (x + w//2, y + h//2), radius = w//2, color = [0,255,0], thickness = 2)

    # 显示图片
    cv2.imshow('video', frame)
    
    # 设置退出键和展示频率
    if ord('q') == cv2.waitKey(40):
        break

# 释放资源
cv2.destroyAllWindows()
cap.release()
