from email.header import Header
from email.mime.text import MIMEText
import smtplib
def(username, password)
username = "qq1553457850@163.com"  # 用户名
password = "a13307023186"

# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "qq1553457850@163.com"  # 用户名
mail_pass = "a13307023186"  # 授权码

sender = 'qq1553457850@163.com'
receivers = ['qq1553457850@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')

message['From'] = Header("菜鸟教程", 'utf-8')  # 括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
message['To'] = Header("测试", 'utf-8')  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

subject = 'Python SMTP 邮件测试'
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
