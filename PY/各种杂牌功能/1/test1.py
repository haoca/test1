# print(2**38)
import time
c = r'''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''
# for i in c:
#     a = i
#     print('{}'.format(a), a)
byte = c
ac = c
list1 = []
print(len(byte))
a = [0]*len(byte)
for i in range(len(byte)):
    if byte[i] == ' ':
        a[i] = ' '
    elif byte[i] == 'y':
        a[i] = 'a'
    elif byte[i] == 'z':
        a[i] = 'b'
    else:
        a[i] = byte[i]
    # byte[i] = ord(byte[i])+2
        a[i] = chr(ord(a[i])+2)

    # print(a[i])
str3 = ''.join(a)
# print(str3)


def sleep_in(weekday, vacation):
    if (weekday != 0) & (vacation == 0):
        return 0

    else:
        return


# print(sleep_in(1, 1))


def string_times(str, n):

    return str[0:3]*n


# print(string_times('hiloiuy', 3))
# time.sleep(1)
def missing_char(str, n):
    return str[0:n]+str[n+1:]


str = 'n3456'

print(str[0:len(str)])
print(len(str))
print(str[0:-1])
