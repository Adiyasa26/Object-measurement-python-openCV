import cv2
from numpy import angle
from object_detector import *
import numpy as np
import time
import csv

img = cv2.imread("/home/adiyasa/image-measurement-app/measure/koex.jpeg")

detector = HomogeneousBgDetector()

contours = detector.detect_objects(img)

header = ['file_name', 'x', 'y', 'width' , 'height', 'angle']

with open('data.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

for cnt in contours:
    # Get rect
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = rect

    file_name = "result_{}.jpg".format(int(time.time()))

    data = []

    data.extend([file_name, x, y, w, h, angle])

    with open('data.csv', 'a+', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the data
        writer.writerow(data)

    # display rectangle
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    cv2.circle(img, (int(x), int(y)), 5, (0, 0, 255), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 2)
    cv2.putText(img, "Width {}".format(round(w, 1)), (int (x), int(y - 20)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2) 
    cv2.putText(img, "Height {}".format(round(h, 1)), (int (x), int(y + 15)), cv2.FONT_HERSHEY_PLAIN, 2, (100, 200, 0), 2) 

#save image with measurement
cv2.imwrite("/test_output/result_{}.jpg".format(int(time.time())), img)
cv2.waitKey(0)

