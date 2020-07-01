#coding:utf-8
import urllib, sys
import ssl
import json
import base64
import cv2
global token
# 保证兼容python2以及python3
IS_PY3 = sys.version_info.major == 3
if IS_PY3:
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.error import URLError
    from urllib.parse import urlencode
    from urllib.parse import quote_plus
else:
    import urllib.request
    from urllib import quote_plus
    from urllib.request import urlopen
    from urllib.request import Request
    from urllib.request import URLError
    from urllib import urlencode

 
def getToken():
    global token
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=你的API Key&client_secret=你的Secret Key'
    request = urllib.request.Request(host)
    request.add_header('Content-Type', 'application/json; charset=UTF-8')
    response = urllib.request.urlopen(request)
    content = response.read()
    if (content):
        token=json.loads(content)['access_token']
 
def faceDetect(imgBase64):
    '''
    人脸检测与属性分析
    '''
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    request_url = request_url + "?access_token=" + token
    request = urllib.request.Request(request_url)
    request.add_header('Content-Type', 'application/json')
    data = {"image": imgBase64, "image_type": "BASE64","face_field":"age,beauty,expression,face_shape,gender"}
    response = urllib.request.urlopen(request, urllib.urlencode(data))
    content = response.read()
    if content:
        return content
 
def imgToBase64(imgPath):
    with open(imgPath, "rb") as f:  # 转为二进制格式
        base64_data = base64.b64encode(f.read())  # 使用base64进行加密
        return base64_data
 
 
if __name__=="__main__":
 
    getToken()
    imgPath=r"C:\Users\lee\Pictures\lena.jpg"
    result=json.loads(faceDetect(imgToBase64(imgPath)))['result']
    face_list=result['face_list'][0]
    location=face_list['location']
    age=face_list['age']
    beauty=face_list['beauty']
    expression=face_list['expression']['type']
    gender=face_list['gender']['type']
 
    img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
    leftTopX=int(location['left'])
    leftTopY=int(location['top'])
    rightBottomX=int(leftTopX+int(location['width']))
    rightBottomY = int(leftTopY + int(location['height']))
    cv2.rectangle(img, (leftTopX, leftTopY), (rightBottomX, rightBottomY), (0, 255, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # 第一个坐标表示起始位置
    cv2.putText(img,"age:"+str(age),(0, 20),font, 0.5, (200, 255, 255), 1)
    cv2.putText(img, "gender:" + gender.encode("utf-8"), (0, 40), font, 0.5, (200, 255, 255), 1)
    cv2.putText(img, "beauty:" + str(beauty), (0, 60), font, 0.5, (200, 255, 255), 1)
    cv2.putText(img, "expression:" + str(expression), (0, 80), font, 0.5, (200, 255, 255), 1)
    cv2.imshow('image', img)
    cv2.waitKey(0)
 
    print("end")