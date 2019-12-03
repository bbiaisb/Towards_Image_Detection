import cv2 as cv

def faceDetection(img_2):
    # img_2 = cv.imread("Haruki_Murakami.jpg")
    face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray = cv.cvtColor(img_2, cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv.rectangle(img_2, (x, y), (x + w, y + h), (255, 255, 255), 2)
    cv.imshow('img_2', img_2)
    cv.waitKey()
    cv.destroyAllWindows()
    print(gray, img_2)


# img = cv.imread("test.jpg")
img_2 = cv.imread("Haruki_Murakami.jpg")
faceDetection(img_2)
print(type(img_2))

print(faceDetection(img))
