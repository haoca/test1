import base64
import json
import requests
import pprint
# import urllib,urllib.request, sys
import ssl
import cv2
global token

def cap():
    capture = cv2.VideoCapture(0)
    while(True):
    # 获取一帧
        ret, frame = capture.read()
        cv2.imwrite("youtemp.png", frame)
        capture.release() #释放摄像头
        cv2.destroyAllWindows()#删除建立的全部窗口
        break

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
        print(request_url)
        response = requests.post(url=request_url, data=post_data, headers=self.headers)
        json_result = json.loads(response.text)
        pprint.pprint(json_result)
        if json_result['error_msg'] != 'pic not has face':
            #print(json_result['result'])
            print("图片中包含人脸数：", json_result['result']['face_num'])
            print("图片中包含人物年龄：", json_result['result']['face_list'][0]['age'])
            print("图片中包含人物颜值评分：", json_result['result']['face_list'][0]['beauty'])
            print("图片中包含人物性别：", json_result['result']['face_list'][0]['gender']['type'])
            print("图片中包含人物种族：", json_result['result']['face_list'][0]['race']['type'])
            print("图片中包含人物表情：", json_result['result']['face_list'][0]['expression']['type'])
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
            imgPath=r'youtemp.png'
            img = cv2.imread(imgPath, cv2.IMREAD_COLOR)
            leftTopX=int(location['left'])
            leftTopY=int(location['top']*0.5)
            rightBottomX=int(leftTopX+int(location['width']))
            rightBottomY = int(leftTopY + int(location['height']*1.15))
            cv2.rectangle(img, (leftTopX, leftTopY), (rightBottomX, rightBottomY), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            # fontpath = "./font/simsun.ttc"
            # font= ImageFont.truetype(fontpath, 30)
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
if __name__ == '__main__':
    cap()
    # img_src = input('请输入需要检测的本地图片路径:')
    img_src = 'youtemp.png'
    baiduDetect = BaiduPicIndentify(img_src)
    result = baiduDetect.detect_face()
    face(result)

    
    
    