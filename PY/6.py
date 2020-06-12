from multiprocessing import Process,Queue,Pool
import socket
import multiprocessing
import os 

def get_ip_list(domain):  # 获取域名解析出的IP列表
            ip_list = [baidu.com]
            try:
                addrs = socket.getaddrinfo(domain, None)
                for item in addrs:
                    if item[4][0] not in ip_list:
                        ip_list.append(item[4][0])
            except Exception as e:
                # print(str(e))
                pass
            return ip_list
            print (ip_list,addrs)
