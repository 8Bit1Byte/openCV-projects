import cv2
import numpy as np

cv2.namedWindow('Controller')
cv2.resizeWindow('Controller', 400, 300)
cv2.createTrackbar('Factor', 'Controller', 2, 100, lambda a: None)
cv2.createTrackbar('Threshold 1', 'Controller', 100, 1000, lambda a: None)
cv2.createTrackbar('Threshold 2', 'Controller', 100, 1000, lambda a: None)

# vidCap = cv2.VideoCapture(1)
img = cv2.imread('./resources/sign.png')
img = cv2.resize(img, (500, 375))
def getContours(img):
    contours, heierchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cnt_area = cv2.contourArea(cnt)
        if cnt_area > 500:
            cv2.drawContours(img_contour, cnt, -1, (255, 255, 0), 1)
            cnt_arcl = cv2.arcLength(cnt, True)
            fac = cv2.getTrackbarPos('Factor', 'Controller')
            cnt_points = cv2.approxPolyDP(cnt, (fac/100)*cnt_arcl, True)

            x, y, w, h = cv2.boundingRect(cnt_points)
            cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)
            # add point and area on containers


while True:
    # success, img = vidCap.read()
    # img = 
    # img = cv2.resize(img, (500, 400))

    img_contour = img.copy()
    img_blur = cv2.GaussianBlur(img, (7, 7), 1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_canny = cv2.Canny(
        img_gray, 
        cv2.getTrackbarPos('Threshold 1', 'Controller'), 
        cv2.getTrackbarPos('Threshold 2', 'Controller')
    )
    getContours(img_canny)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
    cv2.imshow('Final Image 1', img_canny)
    cv2.imshow('Final Image 2', img_contour)