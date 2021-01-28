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

    return all


get_info()

# # def handle(content):
# id = 169284469
# # while id < 169284469:
# idl = str(id)

# f = open("date.ini", "w+")
# str = f.read()
# # if(str.find(login)==-1)
# name = f.write(get_info(idl))


# json_result = json.loads(response.text)
# print(json_result)
# return json_result['access_token']
# id = 169284469
# # while id < 169284469:
# idl = str(id)
# get_info(idl)
# id = id + 1
