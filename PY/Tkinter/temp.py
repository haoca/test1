def open1():
    f = open("38.txt", "a+")

    # if(str.find(login)==-1)
    a = [3, 9]
    for i in range(len(a)):
        c = str(a[i])
        name = f.write(c)
    f.write('\n')


open1()
a = 1.23456789
print('{%.2f}' % a)
