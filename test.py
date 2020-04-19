import numpy as np
import cv2
girl = cv2.imread("/home/hp/girl/testdataset/ashu2.jpg")
girl=cv2.resize(girl,(289,385))
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
found,w = hog.detectMultiScale(girl, winStride=(8,8), padding=(32,32), scale=1.05)
for x, y, w, h in found:
    # the HOG detector returns slightly larger rectangles than the real objes.
    # so we slightly shrink the rectangles to get a nicer output.
    pad_w, pad_h = int(0.15 * w), int(0.05 * h)
    #cv2.rectangle(girl, (x, y), (x + w, y + h), (0, 255, 0), 10)