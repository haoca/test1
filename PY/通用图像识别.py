import base64,os
import json
import requests
import pprint
import cv2
import numpy
from PIL import Image, ImageDraw, ImageFont
global token

def cap1():
        capture = cv2.VideoCapture(0)
        while(True):
        # 获取一帧
            ret, frame = capture.read()
            cv2.imwrite("youtemp.png", frame)
            capture.release() #释放摄像头
            cv2.destroyAllWindows()#删除建立的全部窗口
            break

def cv2ImgAddText(img, text, left, top, textColor=(0, 255, 0), textSize=20):
    if (isinstance(img, numpy.ndarray)):  # 判断是否OpenCV图片类型
        img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(img)
    # 字体的格式
    fontStyle = ImageFont.truetype(
        "font/simsun.ttc", textSize, encoding="utf-8")
    # 绘制文本
    draw.text((left, top), text, textColor, font=fontStyle)
    # 转换回OpenCV格式
    return cv2.cvtColor(numpy.asarray(img), cv2.COLOR_RGB2BGR)


# 
# '''
def usual():
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
            # print(result['access_token'])

# '''
# 通用物体和场景识别
# '''

    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general"
        # 二进制方式打开图片文件
    choose = input('\n请选择图片来源:\nA.本地图片\nB.使用摄像头拍照\n')
    if choose == 'A' or choose == 'a':
        ab = input("本程序识别图片中的文字\n请输入图片名称（带扩展名）:")
    elif choose == 'B' or choose == 'b':
        cap()
        ab = 'youtemp.png'
    else:
        print('error')
    f = open(ab, 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
        # access_token = '[调用鉴权接口获取的token]'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        # pprint.pprint (response.json())
        json_result = json.loads(response.text)
    imgPath=(ab)
    img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
    # face_list=result['result'][0]['keyword']
    an = list(range(5))
    for i in range(len(an)):
        an[i]=json_result['result'][i]['keyword']+'  概率：'+str(json_result['result'][i]['score'])
    
    
    
    img = cv2ImgAddText(img,'@haostart\n标签：' +'\n' +an[0] + '\n' +an[1] + '\n' +an[2]+ '\n' +an[3]+ '\n' +an[4], 0, 10, (200, 255, 255), 25)
    
    
    cv2.imshow('image', img)
    cv2.imwrite("youtemp_analysis.png", img)
    cv2.waitKey(0)


def face1():
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=eQudGxUDtmt6xpaKOUPkhss3&client_secret=VY7ox9Pm6P7WfxY6ZgZOaqgHbEHylIm0'
        response = requests.get(host)
        if response:
        # pprint.pprint(response.json())
            result = response.json()
            access_token = result['access_token']
            print(result['access_token'])
class BaiduPicIndentify:
        def __init__(self, img):
            self.AK = "dflyZoR8kWaWXgXHRqEtrs3S"
            self.SK = "grP0L6VYMhwnvV5soCRtB47N6mZ8ztzE"
            self.img_src = img
            self.headers = {
                "Content-Type": "application/json; charset=UTF-8"
            }

        def get_accessToken(self):
            host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + self.AK + '&client_secret=' + self.SK
            response = requests.get(host, headers=self.headers)
            json_result = json.loads(response.text)
            return json_result['access_token']

        def img_to_BASE64(slef, path):
            with open(path, 'rb') as f:
                base64_data = base64.b64encode(f.read())
                return base64_data

        def detect_face(self):
            # 人脸检测与属性分析
            img_BASE64 = self.img_to_BASE64(self.img_src)
            request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
            post_data = {
                "image": img_BASE64,
                "image_type": "BASE64",
                "face_field": "gender,age,beauty,gender,race,expression",
                "face_type": "LIVE"
            }
            access_token = self.get_accessToken()
            request_url = request_url + "?access_token=" + access_token
            # print(request_url)
            response = requests.post(url=request_url, data=post_data, headers=self.headers)
            json_result = json.loads(response.text)
            # pprint.pprint(json_result)
            if json_result['error_msg'] != 'pic not has face':
                #print(json_result['result'])
                # print("图片中包含人脸数：", json_result['result']['face_num'])
                # print("图片中包含人物年龄：", json_result['result']['face_list'][0]['age'])
                # print("图片中包含人物颜值评分：", json_result['result']['face_list'][0]['beauty'])
                # print("图片中包含人物性别：", json_result['result']['face_list'][0]['gender']['type'])
                # print("图片中包含人物种族：", json_result['result']['face_list'][0]['race']['type'])
                # print("图片中包含人物表情：", json_result['result']['face_list'][0]['expression']['type'])
                return json_result
                
def face(result):
                # result = baiduDetect.detect_face()
                # print(result)
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
                img = cv2ImgAddText(img,"@haostart\n年龄:"+str(age)+'\n'+"性别:" + str(gender)+'\n'+"颜值:" + str(beauty)+'\n'+"表情:" + str(expression)+'\n'+"皮肤种族:" + str(race)+'\n'+"成功了，图像保存为当前文件夹下的\nyoutemp_analysis.png", 0, 10, (200, 255, 255), 25)
                # cv2.putText(img,"age:"+str(age),(0, 40),font, 1, (200, 255, 255), 1)
                # # cv2.putText(img, "gender:" + gender.encode("utf-8"), (0, 40), font, 0.5, (200, 255, 255), 1)
                # cv2.putText(img, "gender:" + str(gender), (0, 80), font, 1, (200, 255, 255), 1)
                # cv2.putText(img, "beauty:" + str(beauty), (0, 120), font, 1, (200, 255, 255), 1)
                # cv2.putText(img, "expression:" + str(expression), (0, 160), font, 1, (200, 255, 255), 1)
                # cv2.putText(img, "race:" + str(race), (0, 200), font, 1, (200, 255, 255), 1)
                # cv2.putText(img, "Success!saved as youtemp_analysis.png", (0, 240), font, 1, (200, 255, 255), 1)
                cv2.imshow('image', img)
                cv2.imwrite("youtemp_analysis.png", img)
                cv2.waitKey(0)
if __name__ == '__main__':
    # cap()
    n=1
    while n :
        print('\n@Haostart\n'+'这是第['+ str(n) +']次。\n')
        n=n+1
        choose = input('请选择你需要的功能:\nA.通用物体识别\nB.进行人脸检测\n')
        if choose == 'A' or choose == 'a':
            usual()
        
        elif choose == 'B' or choose == 'b':
            choose = input('\n请选择图片来源:\nA.本地图片\nB.使用摄像头拍照\n')
            if choose == 'A' or choose == 'a':
                cho = input("本程序识别图片中的文字\n请输入图片名称（带扩展名）:")
            elif choose == 'B' or choose == 'b':
                cap1()
                cho = 'youtemp.png'
            else:
                print('error')
            
            # img_src = input('请输入需要检测的本地图片路径:')
            img_src = cho
            baiduDetect = BaiduPicIndentify(img_src)
            result = baiduDetect.detect_face()
            face(result)
        

    
