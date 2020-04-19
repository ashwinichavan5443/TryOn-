import cv2
import numpy as np

#load cascade
fb_cas = cv2.CascadeClassifier('/home/hp/PycharmProjects/tryOn/haarcascades/haarcascade_lowerbody.xml')
middle_cascade = cv2.CascadeClassifier("/home/hp/PycharmProjects/tryOn/haarcascades/haarcascade_upperbody.xml")


dress = cv2.imread("/home/hp/Downloads/dataset/ghagracholi/ghagra/bridalghagra.png", cv2.IMREAD_UNCHANGED)
bgr = dress[:,:,:3]
gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

# Some sort of processing...
fw=0

#bgr = cv2.cvtColor(bgr, cv2.COLOR_GRAY2BGR)
alpha = dress[:,:,3] # Channel 3
result = np.dstack([bgr, alpha])
result = cv2.resize(result,(300,450))
cv2.imshow("dress",dress)
girl = cv2.imread("/home/hp/girl/girl17.jpg")
girl=cv2.resize(girl,(300,450))
gray = cv2.cvtColor(girl, cv2.COLOR_BGR2GRAY)  # convert video to grayscale
middle_body = middle_cascade.detectMultiScale(
    gray,
    scaleFactor=1.01,
    minNeighbors=1,
    minSize=(1, 1),  # Min size for valid detection, changes according to video size or body size in the video.
    flags=cv2.CASCADE_SCALE_IMAGE
)
lower_body =fb_cas.detectMultiScale(
    gray,
    scaleFactor=1.01,
    minNeighbors=5,
    minSize=(1, 1),  # Min size for valid detection, changes according to video size or body size in the video.
    flags=cv2.CASCADE_SCALE_IMAGE
)
for(mx,my,mw,mh) in middle_body:
   # cv2.rectangle(girl, (mx, my), (mx + mw, my + mh), (0, 255, 0), 6)
    fw = int(mw/2)


for (x,y,w,h) in lower_body:
    cv2.rectangle(girl, (x, y), (x + w, y + h), (0, 255, 0), 6)
    girl = cv2.cvtColor(girl, cv2.COLOR_BGR2BGRA)
    dress = cv2.resize(result, (w, h))
    # girl=cv2.resize(girl,(fw,girl.shape[0]))
    print(fw)
    w, h, c = dress.shape
    for i in range(0, w):
        for j in range(0, h):

            if dress[i, j][3] != 0:
                girl[y + i, x + j-7] = dress[i, j]

cv2.imshow('Detection Window', girl)
cv2.waitKey(0)

