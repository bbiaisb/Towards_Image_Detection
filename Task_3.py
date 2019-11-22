import numpy as np
import cv2

"""Input: Video camera
output: Video with detected Face and Eyes"""
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2) #((255, 0, 0) => blue rectangle
        # roi_gray = gray[y:y + h, x:x + w] #location of the face
        # roi_color = img[y:y + h, x:x + w] # before : => starting point, after : => ending point
        roi_gray = gray[y:y - int((y + h) * 0.7), x:x + w]
        roi_color = img[y:y - int((y + h) * 0.7), x:x + w] #ROi just upper than 70%, so the mouth won't be considered as eye

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release(0)
# cv2.waitKey()  -> stop for cap?
cv2.destroyAllWindows(0)




    # virtuell environement -> terminal source activate opencv
    #dir -> list, > git pull
    #class stores information