# -*-coding:utf-8 -*-
from socket import *
from time import ctime
COD = 'utf-8'
HOST = '127.0.0.1' #服务端ip
PORT = 21566 #服务端端口号
BUFSIZ = 1024
ADDR = (HOST, PORT)
tcpCliSock = socket(AF_INET, SOCK_STREAM) #创建socket对象
tcpCliSock.connect(ADDR) #连接服务器
while True:
    data = input('>>').strip()
    if not data:
        break
    tcpCliSock.send(data.encode('utf-8')) #发送消息
    data = tcpCliSock.recv(BUFSIZ) #读取消息
    data2 = tcpCliSock.recv(BUFSIZ)
    # print("服务端发送的内容:",data2.decode(COD))
    if not data:
        break
    print(data.decode('utf-8'))
    print("服务端发送的内容:",data2.decode(COD))
tcpCliSock.close() #关闭客户端
