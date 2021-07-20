'''
1. We need live data from webcam
2. Do color detection
3. To find place in object lets find counter of that object 
   by which we can approximate the bounding box arround it.
4. Update image by placing color dot here
'''

import cv2
import numpy as np


def getCounters(img):
    contours, heierchy = cv2.findContours(img, cv2.RETR_EXTERNAL,
                                          cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    for cnt in contours:
        cnt_area = cv2.contourArea(cnt)
        if cnt_area > 500:
            # cv2.drawContours(img_contour, cnt, -1, (0, 0, 255), 3)
            cnt_peri = cv2.arcLength(cnt, True)
            cnt_edges = cv2.approxPolyDP(cnt, 0.02 * cnt_peri, True)
            x, y, w, h = cv2.boundingRect(cnt_edges)
            # cv2.rectangle(img_contour, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return x+w//2, y


camCap = cv2.VideoCapture(1)
camCap.set(3, 640)
camCap.set(4, 480)
camCap.set(10, 100)
while True:
    success, img = camCap.read()
    img = img[:, ::-1, :]
    img_contour = img.copy()
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_mask = cv2.inRange(img_hsv, np.array([83, 81, 91]),
                           np.array([179, 169, 255]))
    img_final = cv2.bitwise_and(img, img, mask=img_mask)
    x, y = getCounters(img_mask)
    getCounters(img_mask)
    cv2.circle(img_contour, (x, y), 5, (255, 0, 255), cv2.FILLED)
    if (cv2.waitKey(1) & 0xFF == ord('q')) or not success:
        break
    cv2.imshow('Video-1', img_contour)