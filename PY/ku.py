#!/usr/bin/python3
# Filename: ku.py
import pyttsx3
from datetime import datetime



def speak(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()

def time():
    current_date = datetime.now( )
    print('现在时间为:'+str(current_date)[0:-10]+'\n')

# speak('hello, are u ok.')
def judge(login,pas):  #判断是否重复
    sin=1 #判断标志
    s=0
    t=0
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
        if login == accout and pas == password :
            # print('密码正确')
            # return 1
            t=1
            quit
        
    # print(t)
    if t == 1 :
        print('密码正确')
        return 1
    else: 
        print('密码错误')
        return 0


def rejudge(login):  #判断是否重复
    sin=1 #判断标志
    s=0
    t=0
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
            s+=1
            # print(line)
            if(login == name):
                t=s
                sin=0
                # print(sin)
        # print(sin)
    f.close()
    # print(s,t)
    if sin == 0:return t
    else : return 0
def suc():
    print('nj')
def regist(login):
    f = open("date.txt", "a+")
    name = f.write('\n用户名为:'+login)
    psd = f.write('密码为:'+input('请输入密码：')+'\n')
    f.close()
    print('恭喜你，用户保存成功。')

        # print(accout,password)
    #     s+=1
    #         # print(line)
    #     if(login == accout):
    #             t=s
    #             sin=0

    #             # print(sin)
    #     # print(sin)
    # f.close()
    # # print(s,t)
    # if sin == 0:return t
    # else if sin and : return 0
    # else: return 0
# input()
# judge('123','jkl')
# judge('123','456')