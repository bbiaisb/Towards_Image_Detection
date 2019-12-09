import cv2 as cv


def face_protect(img, mean):

    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    for (x, y, w, h) in faces:
        if mean == "blur":
            img[y:y + h, x:x + w] = cv.GaussianBlur(img[y:y + h, x:x + w], (51, 51), 0)

        elif mean == "black":
            img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)

        elif mean == "truth":
            truth = cv.imread("protected_by_truth.png")
            img[y:y + h, x:x + w] = truth[y:y + h, x:x + w]

    return img
