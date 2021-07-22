import cv2
import numpy as np

vidcap = cv2.VideoCapture(1)
# tracker = cv2.TrackerMOSSE_create()
tracker = cv2.TrackerCSRT_create()
success, img = vidcap.read()

while np.all(img[0, 0] == np.array([36, 137, 255])):
    success, img = vidcap.read()
bbox = cv2.selectROI('Object Tracking', img, False)
tracker.init(img, bbox)
while True:
    timer = cv2.getTickCount()
    success, img = vidcap.read()    
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
    # fps = vidcap.get(cv2.CAP_PROP_FPS)
    status, bbox = tracker.update(img)
    x, y, w, h = [int(i) for i in bbox]
    # cv2.boundingRect(bbox)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=1)
    # print(bbox)
    # FPS and Status
    cv2.rectangle(img, (10, 10), (175, 60), (0, 255, 255), thickness=1)
    cv2.putText(img, f'Fps : {int(fps)}', (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255))
    cv2.putText(img, f'Status : {"Tracking" if status else "Not Tracking"}', (15, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0))

    if cv2.waitKey(1) & 0xFF == ord('q') or not success:
        break
    cv2.imshow('Object Tracking', img)
