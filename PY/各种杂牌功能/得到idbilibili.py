
import json
import pprint
import requests
import urllib
import urllib.request
import re


def get_info(idl):
    host = 'https://space.bilibili.com/' + idl
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
    response = requests.get(host, headers)
    content = response.text
    con2 = content
    # print(content)
    start = content.find('description" content="') + 22
    end = content.find('，bilibili是国内知名的视频弹幕网站') - 6
    content = content[start:end+len('</map>')].strip()
    real_content_id = content.find('，')+1
    username = content[:real_content_id-1]
    reg = r'name="description" content="([\s\S]+?)，bilibil'
    # impress = re.compile(reg)

    content2 = re.findall(reg, con2)
    print(reg)
    print(content2)
    # for i in content2:
    #     print(i)

    real_content = content[real_content_id:].replace('\\n', ' ')
#     print('id:' + idl)
#     print(username + '\n' + real_content)
    all = 'id:' + idl + '\nusername:' + username+'\nwrite:'+real_content+'\n'
#     f = open("date.ini", "r+")
    # print(all)
    return all


# def handle(content):
id = 169284469
# while id < 169284469:
idl = str(id)

f = open("date.ini", "w+")
str = f.read()
# if(str.find(login)==-1)
name = f.write(get_info(idl))


# json_result = json.loads(response.text)
# print(json_result)
# return json_result['access_token']
# id = 169284469
# # while id < 169284469:
# idl = str(id)
# get_info(idl)
# id = id + 1
