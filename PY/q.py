# login='abcd1'
# print(login.count('1'))
import os
import threading


def a1():
    # int i1 = 0
    ab = 0
    while ab < 10:
        for i in range(0, 1000):
            i += 1

        print('\nnihao')
        ab += 1


def a2():
    input('please input message:')
    # print('world.\n')


threading.Thread(target=a1, args=()).start()
threading.Thread(target=a2, args=()).start()
