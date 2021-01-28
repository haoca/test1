import cv2
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
import imutils
import pickle
import time
import cv2
import os
import tkinter as tk


def recognize_video():
    # 创建识别窗口
    win_rec = tk.Tk()
    win_rec.title('人脸识别')
    win_rec.geometry('300x320')
    var_name = tk.StringVar()
    var_proba = tk.StringVar()
    var_ans = tk.StringVar()

    # 创建画布用于切换图片
    canvas1 = tk.Canvas(win_rec, height=129, width=183)
    canvas2 = tk.Canvas(win_rec, height=129, width=183)
    stop = tk.PhotoImage(file='stop.gif')
    welcome = tk.PhotoImage(file='welcome.gif')
    canvas1.create_image(0, 0, anchor='nw', image=stop)
    canvas2.create_image(0, 0, anchor='nw', image=welcome)

    # 创建Label用于显示人名及匹配度
    tk.Label(win_rec, text='姓  名:').place(x=50, y=50)
    tk.Label(win_rec, text='匹配度:').place(x=50, y=90)
    tk.Label(win_rec, textvariable=var_name).place(x=100, y=50)
    tk.Label(win_rec, textvariable=var_proba).place(x=100, y=90)
    tk.Label(win_rec, textvariable=var_ans).place(x=100, y=130)
    tk.Label(win_rec, text='人脸识别系统v6').place(x=175, y=300)


print("[INFO] starting video stream...")

cap = cv2.VideoCapture(0)
while True:

    flag, frame = cap.read()
    if flag == False:
        break

    cv2.imshow('video', frame)
cv2.destroyAllWindows()
cap.release()
