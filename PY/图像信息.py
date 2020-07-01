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
json_result = json.loads(response.text)
pprint.pprint(json_result)
# if json_result['error_msg'] != 'pic not has face':
i = 0
print('图片中元素：')
while i < 5 :
            #print(json_result['result'])
    tags = ['','','','','','']
    tags.clear
    tags.append(json_result['result'][i]['keyword'])
    print(tags[i])
    i=i+1
def face(result):
            # result = baiduDetect.detect_face()
            # print(result)
            tags
            face_list=result['result']['face_list'][0]
            location=face_list['location']
            age=face_list['age']
            race=face_list['race']['type']
            beauty=face_list['beauty']
            expression=face_list['expression']['type']
            gender=face_list['gender']['type']
            # imgPath=r"C:\Users\haost\Desktop\temp\PY\l.jpg"
            imgPath=(img_src)
            img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
            leftTopX=int(location['left'])
            leftTopY=int(location['top']*0.5)
            rightBottomX=int(leftTopX+int(location['width']))
            rightBottomY = int(leftTopY + int(location['height']*1.15))
            cv2.rectangle(img, (leftTopX, leftTopY), (rightBottomX, rightBottomY), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            # 第一个坐标表示起始位置
            cv2.putText(img,"age:"+str(age),(0, 40),font, 1, (200, 255, 255), 1)
            # cv2.putText(img, "gender:" + gender.encode("utf-8"), (0, 40), font, 0.5, (200, 255, 255), 1)
            cv2.putText(img, "gender:" + str(gender), (0, 80), font, 1, (200, 255, 255), 1)
            cv2.putText(img, "beauty:" + str(beauty), (0, 120), font, 1, (200, 255, 255), 1)
            cv2.putText(img, "expression:" + str(expression), (0, 160), font, 1, (200, 255, 255), 1)
            cv2.putText(img, "race:" + str(race), (0, 200), font, 1, (200, 255, 255), 1)
            cv2.putText(img, "Success!saved as youtemp_analysis.png", (0, 240), font, 1, (200, 255, 255), 1)
            cv2.imshow('image', img)
            cv2.imwrite("youtemp_analysis.png", img)
            cv2.waitKey(0)