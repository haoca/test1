# !/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.office365.com"  # 设置服务器
mail_user = "haostart@hotmail.com"  # 用户名
mail_pass = "a13307023186"  # 口令


sender = 'haostart@hotmail.com'
receivers = ['qq1553457850@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] = Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
    # smtpObj = smtplib.SMTP()
    smtpObj = smtplib.SMTP_SSL('smtp.office365.com')
    smtpObj.connect(mail_host, port=587)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error: 无法发送邮件")