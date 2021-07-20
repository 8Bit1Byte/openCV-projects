'''
1. DETECT SHAPE AND LABEL THEM OUT
2. NUMBER OF CORNER POINTS
3. AREA OF SHAPE
'''
import cv2
import numpy as np
'''
1. we can think of canny image which for edge
so convert image to grayscale and then canny

2. From this edges we will find counters using [cv2.findContours]
'''

def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

def getCounters(img):
    '''
    1. We need retrival method for finding contours
    cv2.RETR_EXTERNAL mode is best when working with outer details

    2. Then we use [cv2.CHAIN_APPROX_NONE] approximation to avoid approximation
    This will reduce points for us

    3. Make area threshold so that it doesn't detect any noise

    4. Find perimeter(curvelenght) which gives idea about number edges of shapes

    5. Approximates a polygonal curve(s) with the specified precision.
    Approximates a curve or a polygon with another curve/polygon with less vertices 
    so that the distance between them is less or equal to the specified precision.
    '''

    contours, heierchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        cnt_area = cv2.contourArea(cnt)
        if cnt_area > 500:
            cv2.drawContours(img_contour, cnt, -1, (0, 0, 255), 3)
            cnt_peri = cv2.arcLength(cnt, True)
            cnt_edges = cv2.approxPolyDP(cnt, 0.02*cnt_peri, True)
            cnt_edge_no = len(cnt_edges)

            # creating bounding box
            x, y, w, h = cv2.boundingRect(cnt_edges)
            cv2.rectangle(img_contour, (x, y), (x+w, y+h), (0, 255, 0), 2)

            if cnt_edge_no == 3: 
                cnt_name = 'Triangle'
            elif cnt_edge_no == 4: 
                # we have a deviation of 5%
                aspect_ratio = w/float(h)
                if aspect_ratio > 0.95 and aspect_ratio < 1.05:
                    cnt_name = 'Square'
                else:
                    cnt_name = 'Rectangle'
            else: 
                cnt_name = 'Circle'
            
            cv2.putText(img_contour, cnt_name, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0))

img_shape = cv2.imread('./resources/images/shapes.png')
img_contour = img_shape.copy()
img_gray = cv2.cvtColor(img_shape, cv2.COLOR_BGR2GRAY)
# img_blur = cv2.GaussianBlur(img_gray, (7, 7), 1)
img_canny = cv2.Canny(img_gray, 100, 100)
getCounters(img_canny)

img_stack = stackImages(0.6, ([img_shape, img_gray, img_canny], [img_shape, img_gray, img_contour]))
cv2.imshow('Stack Image', img_stack)
cv2.waitKey(0)