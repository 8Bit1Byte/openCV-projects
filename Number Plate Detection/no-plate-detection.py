import cv2
import numpy as np

camCap = cv2.VideoCapture(1)
camCap.set(3, 640)
camCap.set(4, 480)
camCap.set(10, 100)
face_cascade = cv2.CascadeClassifier('./resources/cascade/haarcascade_russian_plate_number.xml')
x, y, w, h = 0, 0, 0, 0
count = 0
while True:
    success, img = camCap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_plates = face_cascade.detectMultiScale(img_gray, 1.1, 4)
    print(img_plates)

    for  (x, y, w, h), i in zip(img_plates, range(len(img_plates))):
        if w*h > 500:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=2)
            cv2.putText(img, f'Plate Number-{i+1}', (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), thickness=2)
            plate = img[y:y+h, x:x+w]

    if cv2.waitKey(1) & 0xFF == ord('s'):
        count += 1
        cv2.imwrite(f'./output/snapshot{count}.jpg', plate)
        cv2.rectangle(img, (100, 100), (200, 200), (255, 255, 0), cv2.FILLED)
        cv2.putText(img, 'Saved', (150, 150), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 3)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break
    cv2.imshow('Video-1', img)