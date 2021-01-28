from urllib import request
import json
import os
import urllib
import urllib.request
import sys
import ssl
import urllib.request
import base64
import cv2
global token
response = urllib.request.urlopen("http://www.baidu.com/")  # 打开网站
# response = response.read()
fi = open("project.txt", 'w')                        # open一个txt文件
page = fi.write(str(json.(response.read())))                # 网站代码写入
fi.close()
os.system('project.txt')
# .\project.txt
print(1)
print('1')
