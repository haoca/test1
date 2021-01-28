from aip import AipImageClassify
import json
import cv2
""" 你的 APPID AK SK """
APP_ID = '20635007'
API_KEY = 'eQudGxUDtmt6xpaKOUPkhss3'
SECRET_KEY = 'VY7ox9Pm6P7WfxY6ZgZOaqgHbEHylIm0'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)


def cap1():
    capture = cv2.VideoCapture(0)
    while(True):
        # 获取一帧
        ret, frame = capture.read()
        cv2.imwrite("b.jpg", frame)
        capture.release()  # 释放摄像头
        cv2.destroyAllWindows()  # 删除建立的全部窗口
        break


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def info():
    image = get_file_content('b.jpg')

    """ 调用图像主体检测 """
    client.objectDetect(image)

    """ 如果有可选参数 """
    options = {}
    options["with_face"] = 0

    """ 带参数调用图像主体检测 """
    print(client.objectDetect(image, options))
    return client.objectDetect(image, options)['result']
# print(client.advancedGeneral(image, options))


def kuang(location):

    img = cv2.imread('b.jpg', cv2.IMREAD_COLOR)
    leftTopX = int(location['left'])
    leftTopY = int(location['top'])
    rightBottomX = int(leftTopX+int(location['width']))
    rightBottomY = int(leftTopY + int(location['height']))
    cv2.rectangle(img, (leftTopX, leftTopY),
                  (rightBottomX, rightBottomY), (0, 255, 0), 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.imshow('image', img)
    cv2.waitKey(0)


cap1()

kuang(info())
