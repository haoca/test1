# import tkinter as tk
from tkinter import *
import requests
import jsonpath
import os
from urllib.request import urlretrieve
import threading
import time


def opendir():

    os.system(r'explorer.exe    '+os.getcwd()+'\\1')

    print(os.getcwd())


def download1(url, file_path, title):
    # 第一次请求是为了得到文件总大小
    r1 = requests.get(url, stream=True, verify=False)
    total_size = int(r1.headers['Content-Length'])

    # 这重要了，先看看本地文件下载了多少
    if os.path.exists(file_path):
        temp_size = os.path.getsize(file_path)  # 本地已经下载的文件大小
    else:
        temp_size = 0
    # 显示一下下载了多少
    print(temp_size)
    print(total_size)
    # 核心部分，这个是请求下载时，从本地文件已经下载过的后面下载
    headers = {'Range': 'bytes=%d-' % temp_size}
    # 重新请求网址，加入新的请求头的
    r = requests.get(url, stream=True, verify=False, headers=headers)

    # 下面写入文件也要注意，看到"ab"了吗？
    # "ab"表示追加形式写入文件
    text.insert(END, '歌曲: {}, 正在下载...\n '.format(
        title))  # 文本框滚动1
    i = 0
    with open(file_path, "ab") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()
                i = i+1

                ###这是下载实现进度显示####
                done = int(50 * temp_size / total_size)
                if done >= 50:
                    print('下载已经完成。')
                    text.insert(END, '下载已经完成。')
                    text.see(END)
                    text.update()  # 下载
                    return
                sys.stdout.write("\r[%s%s] %.2f%%" % (
                    '█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                if i == 10:
                    text.insert(END, '进度 : {%.2f} \n' % (
                        100 * temp_size / total_size))  # 文本框滚动1
                    text.see(END)
                    text.update()  # 下载
                    text.delete(first=1)
                    i = 0

                sys.stdout.flush()
    print()  # 避免上面\r 回车符
    done = 0
    text.insert(END, '下载完毕: {}, 请试听'.format(title))
    text.see(END)
    text.update()  # 下载
    # added_thread2.delete()


def waite():
    while 1:
        text.insert(END, '进度 : {%.2f} \n' % (
            100 * temp_size / total_size))  # 文本框滚动1
        text.see(END)
        text.update()  # 下载
        time.sleep(3)


def insert_point():
    print('123')
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    date = {
        'input': e.get(),
        'filter': 'name',
        'type': var.get(),
        'page': 1,
    }
    url = 'https://music.liuzhijin.cn/'
    rev = requests.post(url=url, data=date, headers=headers)
    jsontxt = rev.json()
    # print(jsontxt)
    # text. (jsontxt)
    title = jsonpath.jsonpath(jsontxt, '$..title')[0]
    anthor = jsonpath.jsonpath(jsontxt, '$..author')[0]
    url = jsonpath.jsonpath(jsontxt, '$..url')[0]
    print(title, url)
    added_thread1 = threading.Thread(target=download1(
        url, '1\\'+title+'.mp3', title), name='T1')
    added_thread1.start()
    # added_thread2 = threading.Thread(target=waite(), name='T2')
    # added_thread2.start()
    # download1(url, '1\\'+title+'.mp3', title)


def insert_end():
    quit()


root = Tk()
root.title('音乐下载器')
root.geometry('500x500+350+100')
label = Label(root, text='请输入音乐名:  ', font=('方正字迹-龙吟体 简', 20))
label.grid()
e = Entry(root, show=None, font=('方正字迹-楷体 简', 20))
e.grid(row=0, column=1)
e.insert(index='123', string='不得不爱')
var = StringVar()
r1 = Radiobutton(root, text='网易云', variable=var,
                 value='netease', font=('楷体', 30))
r1.grid(row=1, column=0)
r1.select()
r2 = Radiobutton(root, text='QQ音乐', variable=var,
                 value='qq', font=('楷体', 30))
r2.grid(row=1, column=1)

text = Listbox(root, font=('楷体', 12), width=60, height=20)
text.grid(row=2, columnspan=2)

b1 = Button(root, text='开始下载', width=15,
            height=2, command=insert_point)
b1.grid(row=3, column=0)

b2 = Button(root, text='打开文件夹', width=15,
            height=2, command=opendir)
b2.grid(row=3, column=1)
root.mainloop()
