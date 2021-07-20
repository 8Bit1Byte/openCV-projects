
import cv2
import numpy as np


def getCounters(img):
    contours, heierchy = cv2.findContours(img, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x, y, w, h = 0, 0, 0, 0
    max_cnt_area = 0
    max_cnt_edges = np.array([])
    max_cnt = None
    for cnt in contours:
        cnt_area = cv2.contourArea(cnt)
        if cnt_area > 5000:
            # cv2.drawContours(img_contour, cnt, -1, (0, 0, 255), 3)
            cnt_peri = cv2.arcLength(cnt, True)
            cnt_edges = cv2.approxPolyDP(cnt, 0.02 * cnt_peri, True)
            if len(cnt_edges) == 4 and cnt_area > max_cnt_area:
                max_cnt_edges = cnt_edges
                max_cnt_area = cnt_area
                max_cnt = cnt
    cv2.drawContours(img_contour, max_cnt, -1, (0, 0, 255), 5)
    return max_cnt_edges

def preProcess(img):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_blur = cv2.GaussianBlur(img_hsv, (7, 7), 1)
    img_canny = cv2.Canny(img_blur, 200, 200)
    kernel = np.ones((5, 5))
    img_dilate = cv2.dilate(img_canny, kernel, iterations=2)
    img_erode = cv2.erode(img_dilate, kernel, iterations=1)
    '''
    Some time lines are thin large so make them dilate or erode as per use
    '''
    return img_erode

def wrapPers(img, img_contour_max):
    pts_1 = np.float32(img_contour_max)
    pts_2 = np.float32([[0, 0], [wind_w, 0], [wind_w, wind_h], [0, wind_h]])
    if pts_1.shape == (0, ):
        pts_1 = np.float32([[0, 0], [0, 0], [0, 0], [0, 0]])
        pers_transform = cv2.getPerspectiveTransform(pts_1, pts_2)
    else:
        pers_transform = cv2.getPerspectiveTransform(pts_1, pts_2)

    img_wrap = cv2.warpPerspective(img, pers_transform, (wind_w, wind_h))
    return img_wrap

camCap = cv2.VideoCapture(1)
wind_w = 640
wind_h = 480
camCap.set(3, wind_w)
camCap.set(4, wind_h)
camCap.set(10, 150)
while True:
    success, img = camCap.read()
    img = img[::-1]
    img_contour = img.copy()
    img_final = preProcess(img)
    img_contour_max = getCounters(img_final)
    # cv2.imshow('Video-1', img_contour)
    # cv2.waitKey(10000)
    img_wrap = wrapPers(img, img_contour_max)

    if (cv2.waitKey(1) & 0xFF == ord('q')) or not success:
        break
    # cv2.imshow('Video-1', img_contour)
    cv2.imshow('Video-2', img_wrap)