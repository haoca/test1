import sys
import os
import tkinter as tk
import base64
import requests
import json


# @haost
def isConnected():

    try:
        html = requests.get("http://www.baidu.com", timeout=2)
        html = str(html.content)
        flag = html.find('www.hao123.com')

        if flag >= 0:
            return 1
        else:
            return 0
    except:
        return False


def get_mac_address():

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


def jiami(password1):

    # 想将字符串转编码成base64,要先将字符串转换成二进制数据
    y_password = password1
    bytes_url = y_password.encode("utf-8")
    h_password = base64.b64encode(bytes_url)
    h_password = r'{B}'+str(h_password)[2:-1]  # 被编码的参数必须是二进制数据
    print('base64加密后:'+h_password)
    return h_password


def mimasave(username, password):

    f = open("foo.ini", "w+")
    str = f.read()

    name = f.write('\n用户名为:'+username+'\n')

    psd = f.write('密码为:'+password+'\n')
    f.close()
    print('恭喜你，用户保存成功。在本文件夹下f00.ini中。\n' +
          'name:'+username+'\npassword:'+password)


def connect():

    mimasave(e1.get(), e2.get())

    s = requests.session()
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


    )
    if isConnected():
        var2.set('恭喜你，登陆成功！！(用户信息已保存)' + '\nname:' +
                 e1.get()+'\npassword:'+e2.get())
    else:
        var2.set('登录失败！！(用户信息已保存)' + '\nname:' +
                 e1.get()+'\npassword:'+e2.get())


def disconnect():

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


    )


def readfile():

    try:
        f = open("foo.ini", "r+")
        for line in f:
            accout_id = line.find('用户名为:')
            pass_id = line.find('密码为:')

            if accout_id != -1:
                name_1 = line[5:-1]
            if pass_id != -1:
                password2 = line[4:-1]

        e1.insert('insert', name_1)
        e2.insert('insert', password2)

        f.close()
    except:
        pass


window = tk.Tk()
window.title('鉴湖宿舍校园网登陆器')

window.geometry('400x250+400+200')


var2 = tk.StringVar()

var = '欢迎使用本软件  @haost'
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


b1 = tk.Button(window, text='登陆/注销', width=15,
               height=2, command=connect).place(x=140, y=90)

var2 = tk.StringVar()
l2 = tk.Label(window, textvariable=var2,
              font=('Arial', 11), width=35, height=5).place(x=24, y=140)

window.mainloop()
