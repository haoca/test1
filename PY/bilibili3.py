from lxml import etree
import base64
import json
import pprint
import requests
import urllib
import urllib.request
import sys
import ssl
import cv2
from html.parser import HTMLParser

from lxml import etree
import requests
from lxml.html import fromstring, tostring
host = 'https://fanyi.baidu.com/#auto/zh/'
# headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
response = requests.get(host)
content = response.text
wb_data = content

# print(content)
html = etree.HTML(wb_data)
str = html.xpath('//*[@id="upload-btn"]/span')
print(html)
print(str)
for i in str:
    print(i)
    for k in i:
        print(k)
# tree1 = html.tostring(html[0])
# 编码'utf-8'
# tree2 = HTMLParser().unescape(tree1.decode('utf-8'))
# print(tree2)
# print(str)
# result = etree.tostring(html)
# print('\n')
# pprint.pprint(result.decode("utf-8"))
