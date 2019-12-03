import cv2 as cv


def face_detection(img):

    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

    #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 255, 255), 2)

    #cv.imshow('img_2', img)
    #cv.waitKey()
    #cv.destroyAllWindows()

    #cv.imwrite("face.jpg", img)
    #im = Image.open("Haru_2.jpg")



    return img



