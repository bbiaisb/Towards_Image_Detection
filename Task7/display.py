import cv2 as cv
from Task7.faceRecognition import faceDetection

img = cv.imread("test.jpg")

print('Original Dimensions : ',img.shape)

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# resize image
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

print('Resized Dimensions : ',resized.shape)

faceDetection(resized)