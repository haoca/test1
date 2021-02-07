#!/usr/bin/python3
# Filename: ku.py
import pyttsx3
from datetime import datetime


def print_hello(name: str) -> str:
    """
    Greets the user by name
        Parameters:
                name (str): The name of the user
        Returns:
                str: The greeting
        """
    print('hello , '+name)


def speak(word: str):
    '''
    Speak words...
        朗读文本。
    '''
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()


def time():
    '''
    return current_date...
        返回当前时间。
    '''
    current_date = datetime.now()
    print('现在时间为:'+str(current_date)[0:-10]+'\n')
    return current_date

# speak('hello, are u ok.')


def judge(login, pas):  # 判断是否重复
    sin = 1  # 判断标志
    s = 0
    t = 0
    f = open("date.txt", "r+")
    # print(sin)
    for line in f:

        accout_id = line.find('用户名为:')
        password_id = line.find('密码为:')
        # final_id = line.find('吧')
        # print(accout_id,password_id)
        # if accout_id != -1:
        accout = line[5:password_id]
        password = line[password_id+4:-1]
        # print(accout,login)
        # print(password,pas)
        if login == accout and pas == password:
            # print('密码正确')
            # return 1
            t = 1
            quit

    # print(t)
    if t == 1:
        print('密码正确')
        return 1
    else:
        print('密码错误')
        return 0


def rejudge(login):  # 判断是否重复
    sin = 1  # 判断标志
    s = 0
    t = 0
    f = open("date.txt", "r+")
    # print(sin)
    for line in f:
        accout_id = line.find('用户名为:')
        password_id = line.find('密码为:')
        # final_id = line.find('吧')
        # print(final_id)
        if accout_id != -1:
            # name = line[5:-1]
            name = line[5:password_id]
            s += 1
            # print(line)
            if(login == name):
                t = s
                sin = 0
                # print(sin)
        # print(sin)
    f.close()
    # print(s,t)
    if sin == 0:
        return t
    else:
        return 0


def regist(login):
    f = open("date.txt", "a+")
    name = f.write('\n用户名为:'+login)
    psd = f.write('密码为:'+input('请输入密码：')+'\n')
    f.close()
    print('恭喜你，用户保存成功。')


def download(url, file_path):
    # 第一次请求是为了得到文件总大小
    r1 = requests.get(url, stream=True, verify=False)
    total_size = int(r1.headers['Content-Length'])

    # 这重要了，先看看本地文件下载了多少
    if os.path.exists(file_path):
        temp_size = os.path.getsize(file_path)  # 本地已经下载的文件大小
    else:
        temp_size = 0
    # 显示一下下载了多少
    print(temp_size+'/')
    print(total_size)
    # 核心部分，这个是请求下载时，从本地文件已经下载过的后面下载
    headers = {'Range': 'bytes=%d-' % temp_size}
    # 重新请求网址，加入新的请求头的
    r = requests.get(url, stream=True, verify=False, headers=headers)

    # 下面写入文件也要注意，看到"ab"了吗？
    # "ab"表示追加形式写入文件
    with open(file_path, "ab") as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                temp_size += len(chunk)
                f.write(chunk)
                f.flush()

                ###这是下载实现进度显示####
                done = int(50 * temp_size / total_size)
                sys.stdout.write("\r[%s%s] %d%%" % (
                    '█' * done, ' ' * (50 - done), 100 * temp_size / total_size))
                sys.stdout.flush()
    print()  # 避免上面\r 回车符
