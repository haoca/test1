import os
import sys
import base64
import json
import pprint
import requests
import urllib
import urllib.request
import sys
import ssl
import cv2


def get_info():
    host = 'https://github.com/haoca/C/blob/master/README.md'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    response = requests.get(host, headers)
    content = response.text
    # print(content)
    start = content.find('abc.') + 4
    end = content.find('.abc')
    content = content[start:end].strip()

    return content


# ip = 'www.baidu.com'
# # 实现pingIP地址的功能，bai-c1指发送报文一次，du-w1指等zhi待1秒
# backinfo = os.system('ping  %s' % ip)
# print(backinfo)
# if backinfo:
#     print('no')
# else:
#     print(ip)
try:
    print(get_info())
except:
    pass
