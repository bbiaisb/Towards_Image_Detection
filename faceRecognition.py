import cv2 as cv

def faceDetection(img):
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv.imshow('img', img)
    cv.waitKey()
    cv.destroyAllWindows()

img = cv.imread("test.jpg")

faceDetection(img)
