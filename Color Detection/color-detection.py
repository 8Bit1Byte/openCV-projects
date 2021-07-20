'''
1. FOR COLOR DETECTION WE NEED [HSV COLOR SPACE]
2. Then we control hue, staturation, and value to get mask for that color
3. Use cv2.cvtColor
'''

import cv2
import numpy as np

def empty(a):
    pass

# create a window
cv2.namedWindow('Controler')
cv2.resizeWindow("Controler", 640, 240)
# creating trackbar
cv2.createTrackbar("Hue Min", "Controler", 0, 179, empty)
cv2.createTrackbar("Hue Max", "Controler", 36, 179, empty)
cv2.createTrackbar("Sat Min", "Controler", 152, 255, empty)
cv2.createTrackbar("Sat Max", "Controler", 255, 255, empty)
cv2.createTrackbar("Val Min", "Controler", 57, 255, empty)
cv2.createTrackbar("Val Max", "Controler", 255, 255, empty)

img = cv2.imread('./resources/images/lamborghini-huracan.jpg')
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:    
    h_min = cv2.getTrackbarPos("Hue Min", "Controler")
    h_max = cv2.getTrackbarPos("Hue Max", "Controler")
    s_min = cv2.getTrackbarPos("Sat Min", "Controler")
    s_max = cv2.getTrackbarPos("Sat Max", "Controler")
    v_min = cv2.getTrackbarPos("Val Min", "Controler")
    v_max = cv2.getTrackbarPos("Val Max", "Controler")
    # print(h_min, h_max, s_min, s_max, v_min, v_max)
    img_mask = cv2.inRange(img_hsv, np.array([h_min, s_min, v_min]), np.array([h_max, s_max, v_max]))
    img_final = cv2.bitwise_and(img, img, mask=img_mask)

    # cv2.imshow('Image RGB', img)
    # cv2.imshow('Image HSV', img_hsv)
    cv2.imshow('Image Mask', img_mask)
    cv2.imshow('Image Final', img_final)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break