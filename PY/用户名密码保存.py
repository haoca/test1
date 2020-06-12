import pyttsx3
from datetime import datetime
current_date = datetime.now( )

def speak(word):
    engine = pyttsx3.init()
    engine.say(word)
    engine.runAndWait()

def judge(login):  #判断是否重复
    sin=1 #判断标志
    s=0
    t=0
    f = open("foo.txt", "r+")
    # print(sin)
    for line in f:
        accout_id = line.find('用户名为:')
        # final_id = line.find('吧')
        # print(final_id)
        if accout_id != -1:
            name = line[5:-1]
            s+=1
            # print(s)
            if(login == name):
                t=s
                sin=0
                # print(sin)
        # print(sin)
    f.close()
    # print(s,t)
    if sin == 0:return t
    else : return 0

print('现在时间为:'+str(current_date)[0:-10]+'\n')
speak('现在时间为:'+str(current_date)[0:-10])
# 创建一个文件
f = open("foo.txt", "a+")
f.close()
login = input('请输入用户名,检查是否可用：')
# if(judge(login)): 
while judge(login):
    login = input('用户名与【{}】重复，请重新输入用户名：'.format(judge(login)))
print('恭喜你，用户名可用。')
f = open("foo.txt", "r+")
str = f.read()
# if(str.find(login)==-1)
name = f.write('\n用户名为:'+login+'\n')
# name = f.write('\n用户名为:'+input('请输入用户名：')+'\n')
psd = f.write('密码为:'+input('请输入密码：')+'\n')
print('恭喜你，用户保存成功。在本文件夹下f00.txt中。')
# else:

# print(num)
# 关闭打开的文件
f.close()