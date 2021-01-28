import cv2


def cap1():
    capture = cv2.VideoCapture(0)
    while(True):
        # 获取一帧
        ret, frame = capture.read()
        cv2.imwrite("b.jpg", frame)
        capture.release()  # 释放摄像头
        cv2.destroyAllWindows()  # 删除建立的全部窗口
        break


cap1()
