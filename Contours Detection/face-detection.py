'''
1. A METHOD FOR FACE DETECTION PERPOSED BY : VIOLA AND JONES
2. Earlist method for realtime object detection

3.
[Postive Image] 
    +              => [Model Train]   => [XML File(Cascade File)]
[Negitive Image]

4. We are going to use PRETRAIN cascade file provide files
5. OpenCV provide some default cascade for face, number plate and many more things
6. Creating Custom cascade files

'''

import cv2

face_cascade = cv2.CascadeClassifier('./resources/cascade/haarcascade_frontalface_default.xml')
img = cv2.imread('./resources/images/face1.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

for face in img_faces:
    x, y, w, h = face
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)

cv2.imshow('Face Image', img)
cv2.waitKey(0)