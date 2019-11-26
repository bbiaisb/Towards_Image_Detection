import cv2 as cv
from PIL import Image

def faceDetection(img):
    img_2 = cv.imread("Haruki_Murakami.jpg")
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)
    #cv.imshow('img_2', img)
    #cv.waitKey()
    #cv.destroyAllWindows()
    cv.imwrite("Haru_2.jpg", img)
    im = Image.open("Haru_2.jpg")
    im.show()

    return cv.imwrite("Haru_2.jpg", img)


img = cv.imread("test.jpg")
img_2 = cv.imread("Haruki_Murakami.jpg")
faceDetection(img_2)

