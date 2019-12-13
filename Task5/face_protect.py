# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 16:54:54 2019

@author: FW
"""

# this is the very much simplyfied version of the function "face_protect" of the doc "Task5"
# this version was used on the flask GUI

import cv2 as cv


def face_protect(img, mean):

    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(img, 1.1, 4)

    for (x, y, w, h) in faces:
        if mean == "blur":
            kernel = int(0.6*w)
            if kernel%2 == 0:
                kernel+=1
            img[y:y + h, x:x + w] = cv.GaussianBlur(img[y:y + h, x:x + w], (kernel,kernel), 0)

        elif mean == "black":
            img = cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), -1)

        elif mean == "truth":
            truth = cv.imread("protected_by_truth.png")
            img[y:y + h, x:x + w] = truth[y:y + h, x:x + w]

    return img
            

