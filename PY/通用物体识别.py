# encoding:utf-8
# import sys
import json,cv2
import base64
import requests,pprint

def cap():
    capture = cv2.VideoCapture(0)
    while(True):
    # 获取一帧
        ret, frame = capture.read()
        cv2.imwrite("youtemp.png", frame)
        capture.release() #释放摄像头
        cv2.destroyAllWindows()#删除建立的全部窗口
        break

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=eQudGxUDtmt6xpaKOUPkhss3&client_secret=VY7ox9Pm6P7WfxY6ZgZOaqgHbEHylIm0'
response = requests.get(host)
if response:
    # pprint.pprint(response.json())
    result = response.json()
    access_token = result['access_token']
    print(result['access_token'])
'''
通用物体和场景识别
'''

request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
# 二进制方式打开图片文件
choose = input('\n请选择图片来源:\nA.本地图片\nB.使用摄像头拍照\n')
if choose == 'A':
    a = input("本程序识别图片中的文字\n请输入图片名称（带扩展名）:")
elif choose == 'B':
    cap()
    a = 'youtemp.png'
else:
    print('error')
f = open(a, 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
# access_token = '[调用鉴权接口获取的token]'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    pprint.pprint (response.json())

