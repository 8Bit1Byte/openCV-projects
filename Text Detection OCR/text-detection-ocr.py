import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread('./resources/test.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_h, img_w = img.shape[:-1]
# print(pytesseract.image_to_string(img))
# print(pytesseract.image_to_boxes(img))
def draw_letter_box():
    for i in map(str.split, pytesseract.image_to_boxes(img).split('\n')[:-1]):
        print(i)
        x, y, w, h = [int(i[j]) for j in range(1, 5)]
        print(x, y, w, h)
        cv2.rectangle(img, (x, img_h - y), (w, img_h - h), (0, 0, 255), thickness=2)
    cv2.imshow('OCR Detection', img)
    cv2.waitKey(0)

def draw_word_box():
    # config = r'--oem 3 --psm 6 outputbase digits'
    lines = pytesseract.image_to_data(img, config= '').splitlines()[1:]
    for i in lines:
        j = i.split('\t')
        if j[11] != '':
            x, y, w, h = int(j[6]), int(j[7]), int(j[8]), int(j[9])
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), thickness=2)
    # for i in map(str.split, pytesseract.image_to_data(img).split('\n')[:-1]):
    #     print(i)
    #     x, y, w, h = [int(i[j]) for j in range(1, 5)]
    #     print(x, y, w, h)
    #     cv2.rectangle(img, (x, img_h - y), (w, img_h - h), (0, 0, 255), thickness=2)
    # cv2.imshow('OCR Detection', img)
    # cv2.waitKey(0)

draw_word_box()
cv2.imshow('Image', img)
cv2.waitKey(0)

# vidcap = cv2.VideoCapture('./resources/test.mp4')

# while True:
#     success, img = vidcap.read()
#     img = cv2.resize(img, (1000, 600))

#     if cv2.waitKey(1) & 0xFF == ord('q') or not success:
#         break

#     cv2.imshow('Video', img)