# 创建一个文件
f = open("date.txt", "a+")
f.close()

from ku import *

from datetime import datetime
current_date = datetime.now( )
# the now function returns a datetime object
print('现在时间为:'+str(current_date)[0:-10]+'\n')


login = input('请输入用户名：')
if rejudge(login)==0: 
    print('检查到您未注册，是否立即注册？\n')
    i = input('a.YES (按其它任意键退出)\n')
    if i==('a') or i=='A':regist(login)
    else: quit()
else:
    pas = input('请输入密码：')
    # print(pas)
    
    while judge(login,pas) == 0:
        pas = input('请重新输入密码：')

print('恭喜你，成功登陆.')

f.close()