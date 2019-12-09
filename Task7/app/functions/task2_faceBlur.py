import cv2 as cv


def face_blur(img):

    img = cv.GaussianBlur(img, (59, 59), 0)

    return img
