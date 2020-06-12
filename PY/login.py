# 创建一个文件
f = open("date.txt", "a+")
f.close()


from datetime import datetime
current_date = datetime.now( )
# the now function returns a datetime object
print('现在时间为:'+str(current_date)[0:-10]+'\n')

def judge(login):  #判断是否重复
    sin=1 #判断标志
    s=0
    t=0
    f = open("date.txt", "r+")
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
def suc():
    print('nj')
def regist(login):
    f = open("date.txt", "r+")
    name = f.write('\n用户名为:'+login)
    psd = f.write('密码为:'+input('请输入密码：')+'\n')
    f.close()
    print('恭喜你，用户保存成功。')

login = input('请输入用户名：')
if judge(login)==0: 
    print('检查到您未注册，是否立即注册？\n')
    i = input('a.YES (按其它任意键退出)\n')
    if i==('a') or i=='A':regist(login)
    else: quit()
else:
    pwd = input('请输入密码：')
    if pwd == ''
    print()


print('恭喜你，登陆成功！')

f = open("date.txt", "r+")
str = f.read()
# if(str.find(login)==-1)
name = f.write('\n用户名为:'+login+'\n')
# name = f.write('\n用户名为:'+input('请输入用户名：')+'\n')
psd = f.write('密码为:'+input('请输入密码：')+'\n')
print('恭喜你，用户保存成功。')


# print(num)
# 关闭打开的文件
f.close()