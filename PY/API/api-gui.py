import base64
import requests
import json
import urllib
import sys
import ssl
import tkinter as tk

window = tk.Tk()
window.title('计算器')

window.geometry('300x300')

var = tk.StringVar()
l = tk.Label(window, textvariable=var,
             font=('Arial', 12), width=30, height=2).place(x=50, y=60)
# l.pack()
on_hit = False
var.set('1')


def hit_me():
    url = 'http://hn216.api.yesapi.cn/?s=App.Open_Baidu.LocationIP&return_data=0&app_key=5EB7C6FD54CF9CDD7A442F0FEC24AB04&sign=E70E38BAB6CFE7B9C9C2D3299BDD5135'

    s = requests.session()

    res1 = s.get(url).text

    res2 = json.loads(res1)['data']['ip']
    print(res2)
    var.set(res2)


b = tk.Button(window, text='your ip address', width=15,
              height=2, command=hit_me).place(x=10, y=60)

c = tk.Button(window, text='your address', width=15,
              height=2, command=hit_me).place(x=10, y=10)
# c.pack()
window.mainloop()
