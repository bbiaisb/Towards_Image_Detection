import cv2 as cv


def face_protect(img, mean):

    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    for (x, y, w, h) in faces:
        if mean == "blur":
            kernel = int(0.55 * w)
            if kernel % 2 == 0:
                kernel += 1
            img[y:y + h, x:x + w] = cv.GaussianBlur(img[y:y + h, x:x + w], (kernel, kernel), 0)

        elif mean == "weak":
            kernel = int(0.08 * w)
            if kernel % 2 == 0:
                kernel += 1
            img[y:y + h, x:x + w] = cv.GaussianBlur(img[y:y + h, x:x + w], (kernel, kernel), 0)

        elif mean == "black":
            img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)

    return img
