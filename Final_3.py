
import cv2
from matplotlib import pyplot as plt
import numpy as np
import  sys



class FaceDetection(object):

    def __init__(self, file):
        self.file = file

        self.img_bgr = cv2.imread(self.file, cv2.IMREAD_COLOR)      #to store arguments

    def BGRtoRGB(self):
        b, g, r = cv2.split(self.img_bgr)
        img_rgb = cv2.merge([r, g, b])

        return img_rgb

    def BRGtoGray(self):
        img_gray = cv2.cvtColor(self.img_bgr, cv2.COLOR_BGR2GRAY)

        return img_gray


    def showImage(self, image):
        plt.axis('on')
        plt.imshow(image)
        plt.title(self.file)
        plt.show()


    def faceRecognition(self, scaleFactor =1.05, minNeighbors =6):

        COLOR_FACE = (255, 0, 255)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(self.BRGtoGray(), scaleFactor, minNeighbors)
        ti_rgb = self.BGRtoRGB()
        for (x, y, w, h) in faces:
            cv2.rectangle(ti_rgb, (x, y), (x + w, y + h), COLOR_FACE, 2)

        print("Anzahl erkannte Gesichter:", len(faces))
        self.showImage(ti_rgb)          # GUI do not need this
        return ti_rgb


    def faceEyeRecognition(self,size = 0.9, scaleFactor =1.05, minNeighbors =6 ):
        COLOR_FACE = (255, 0, 255)
        COLOR_EYES = (255, 0, 0)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(self.BRGtoGray(), scaleFactor, minNeighbors)

        count_faces = 0
        ti_gray = self.BRGtoGray()
        ti_rgb = self.BGRtoRGB()
        for (x, y, w, h) in faces:
            roi_gray = ti_gray[y:y - int((y + h) * size), x:x + w]
            roi_color = ti_rgb[y:y - int((y + h) * size), x:x + w]

            eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
            eyes = eye_cascade.detectMultiScale(roi_gray)
            count_faces += len(eyes) // 2
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), COLOR_EYES, 2)


                if len(eyes) != 0:
                    cv2.rectangle(ti_rgb, (x, y), (x + w, y + h), COLOR_FACE, 2)

        print("number of recognized faces:", count_faces)
        self.showImage(ti_rgb)
        return ti_rgb



class Image(object):
    def __int__(self, img):
        self.img = cv2.imread(img)
    # print(FaceDetecion.faceRecognition("Gruppenfotos_1.jpg"))
        self.classifier = FaceDetection(img)
    # a = classifier.faceRecognition()





def main(img):


    input_image = Image(img)
    classifier = FaceDetection()
    coordinates = classifier.faceEyeRecognition(input_image)




if __name__=='__main__':

    file_path = sys.argv[1]



    main(file_path)
