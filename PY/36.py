# 打开一个文件
f = open("66.txt", "a+")
str = f.read()
# print(type(str))
login = 'nihao'
for line1 in f:
    accout_id = line1.find('用户名为:') + 5
    print(accout_id)
    print(line1, end='')
f.close()
import this