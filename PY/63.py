import numpy as np
import cv2

cap = cv2.VideoCapture('4.mp4')

while (cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break
    # if cv2.waitKey(40) & 0xFF == ord('s'):
    #     cv2.waitKey(0)

cap.release()
cv2.destroyAllWindows()
