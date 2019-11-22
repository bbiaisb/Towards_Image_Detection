import cv2 as cv
from faceRecognition import faceDetection

img = cv.imread("test.jpg")

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)

faceDetection(resized)