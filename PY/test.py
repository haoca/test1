import numpy
from PIL import Image, ImageDraw, ImageFont
import string, random
import base64,os
import json
import requests
import pprint
# import urllib,urllib.request, sys
# import ssl
import cv2
global token

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

def capinfoa(cho):
    while cap.isOpened():
        ret, frame = cap.read()
        
        
        framep = cv2ImgAddText(frame,"@haostart\n退出: “q”键"+'\n'+"进行识别: “s” 键", 0, 10, (200, 255, 255), 25)
    #     cv2.putText(frame,"quit/exit:Press \'q\'",(0, 40),font, 1, (200, 255, 255), 1)
    # # cv2.putText(img, "gender:" + gender.encode("utf-8"), (0, 40), font, 0.5, (200, 255, 255), 1)
    #     cv2.putText(frame, "recognize:Press \'s\'", (0, 80), font, 1, (200, 255, 255), 1)
        cv2.imshow('frame',framep)

        key = cv2.waitKey(delay=40)
        if  0xFF == ord('q'):
            break
        elif key == ord('s'):
            waitKey(delay = 10)
            ran = id_generator()
            cv2.imwrite(ran + '.jpg', frame)
            img_src = ran + '.jpg'
            baiduDetect = BaiduPicIndentify(img_src)
            result = baiduDetect.detect_face()
            face(result,ran,img_src)
            
            os.system("del "+img_src)
    cap.release()
    cv2.destroyAllWindows()
def capinfob():
    while cap.isOpened():
        ret, frame = cap.read()
        # print('frame.shape:', frame.shape)
        font = cv2.FONT_HERSHEY_SIMPLEX
        framep = cv2ImgAddText(frame,"@haostart\n退出: “q”键"+'\n'+"进行识别: “s” 键", 0, 10, (200, 255, 255), 25)
        cv2.imshow('frame',framep)

        key = cv2.waitKey(delay=1)
        if key == ord('q'):
            break
        elif key == ord('s'):
            ran = id_generator()
            cv2.imwrite(ran + '.jpg', frame)
            img_src = ran + '.jpg'
            baiduDetect = BaiduPicIndentify(img_src)
            result = baiduDetect.detect_face()
            face(result,ran,img_src)
            
            os.system("del "+img_src)
    cap.release()
    cv2.destroyAllWindows()

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
 
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
            
def face(result,ran,img_src):
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
            img = cv2ImgAddText(img,"@haostart\n年龄:"+str(age)+'\n'+"性别:" + str(gender)+'\n'+"颜值:" + str(beauty)+'\n'+"表情:" + str(expression)+'\n'+"皮肤种族:" + str(race)+'\n'+"成功了，图像保存为当前文件夹下的\n"+ran+'analysis.jpg', 0, 10, (200, 255, 255), 25)
            
            cv2.imshow('image', img)
            cv2.imwrite(ran + 'analysis.jpg', img)
            # cv2.waitKey(0)
while 1:
    choose = input('\n请选择视频来源:\nA.本地视频\nB.使用摄像头拍摄\n')
    if choose == 'A' or choose == 'a':
                    cho = input("@haostart\n本程序识别图片中的人脸\n请输入视频名称（带扩展名）:")
                    
                    cap = cv2.VideoCapture(cho)
                    if (cap.isOpened()==0):
                        print('\n打开文件失败，请检查文件是否存在。')
                    else:
                        while 1:
                            cap = cv2.VideoCapture(cho)
                            capinfoa(cho)          
                    # print(cap)

    elif choose == 'B' or choose == 'b':
                    cap = cv2.VideoCapture(0)
                    typp = 'frame'
                    capinfob()
    else:
                    print('error')

    cap.release()
    cv2.destroyAllWindows()
