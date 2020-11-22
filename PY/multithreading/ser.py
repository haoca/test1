import socket
from threading import Thread

s = socket.socket()
s.bind(('127.0.0.1', 8010))
s.listen(5)


def run(conn):
    while True:
        try:
            data = conn.recv(1024)
            print(data)
            conn.send(data.upper())
        except Exception:
            break


if __name__ == '__main__':
    while True:
        print('等待客户端连接')
        conn, addr = s.accept()
        print(f'客服端{addr}连接成功')
