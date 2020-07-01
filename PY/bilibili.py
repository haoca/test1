import base64
import json,pprint
import requests
import urllib,urllib.request, sys
import ssl
import cv2


def get_info(idl):
        host = 'https://space.bilibili.com/' + idl
        headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
        response = requests.get(host,headers)
        content = response.text
        # print(content)
        start=content.find('description" content="') + 22
        end=content.find('，bilibili是国内知名的视频弹幕网站') - 6
        content=content[start:end+len('</map>')].strip()
        print('id:' + idl)
        print(content  + '\n')
        # json_result = json.loads(response.text)
        # print(json_result)
        # return json_result['access_token']
id = 169284469
# while id < 169284469:
idl = str(id)
get_info(idl)
id = id +1