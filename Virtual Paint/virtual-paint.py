'''
1. We need live data from webcam
2. Do color detection
3. Update image by placing color dot here
'''

import cv2

def webCamOper():    
    camCap = cv2.VideoCapture(0)
    camCap.set(3, 640)
    camCap.set(4, 480)
    camCap.set(10, 100)
    while True:
        success, img = camCap.read()
        if (cv2.waitKey(100) & 0xFF == ord('q')) or not success:
            break
        cv2.imshow('Hello Video', img)


if __name__ == '__main__':
    webCamOper()