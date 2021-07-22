import cv2
import numpy as np
from pyzbar.pyzbar import decode

def show_data(obj):
    print(obj.data, obj.data.decode('utf-8'))
    print(obj.type)
    print(obj.rect)
    print(obj.polygon)
    print()


img = cv2.imread('./resources/multi_code.png')
img_decode = decode(img)

for bar_code in img_decode:
    # print(bar_code)
    pts = np.array([bar_code.polygon], dtype= np.int32)
    pts = pts.reshape((-1, 1, 2))
    # print(pts)]
    # print(bar_code.rect[0])

    cv2.polylines(img, [pts], True, (0, 255, 0), thickness=2)

cv2.imshow('Barcode Scaned', img)
cv2.waitKey(0)
'''
    FOR REAL TIME QR AND BARCODE SCANNER
vidcap = cv2.VideoCapture(1)

while True:
    success, img = vidcap.read()

    if cv2.waitKey(1) & 0xFF == ord('q') or not success:
        break

    cv2.imshow('QR and Bar Code Scanner', img)
'''