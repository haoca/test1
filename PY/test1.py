import ku
# ku.print_hello(input("please input your name:\n"))
import dis


def func(a, b):
    a, b = b, a
    print(a, b)


a = 10
b = 20


def func(x, y, z): return x+y+z


# 匿名
# 与函数有相同的作用域，但是匿名意味着引用计数为0，使用一次就释放，除非让其有名字 func=lambda x,y,z=1:x+y+z
# lambda x, y, z=1: x+y+z

print(func(1, 2, 3))
#
# x, y, z = 1
print(c=lambda x, y, z=1: x+y+z)
