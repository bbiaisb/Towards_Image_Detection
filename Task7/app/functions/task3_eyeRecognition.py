import cv2


def eye_recognition(img):
    color_eyes = (255, 0, 0)

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=6)
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

    for (x, y, w, h) in faces:
        eyes = eye_cascade.detectMultiScale(img, scaleFactor=1.05, minNeighbors=10)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(img, (ex, ey), (ex + ew, ey + eh), color_eyes, 3)

    return img
