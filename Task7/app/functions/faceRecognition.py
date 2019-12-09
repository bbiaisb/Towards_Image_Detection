import cv2 as cv


def face_detection(img):

    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

    #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (220, 100, 46), 10)

    return img
