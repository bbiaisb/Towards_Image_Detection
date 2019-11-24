import cv2
import numpy as np
from matplotlib import pyplot as plt
import glob
import os


class FaceRecognition(object):
    def __int__(self):
        pass

   def faceRecognition(self, folder):

    """ input: folder with *.jpg data
    output:
    - count of recognized faces
    - image with framed faces """

    COLOR_FACE = (255, 0, 255)
    # Bildordner bestimmen und Dateien auslesen
    # pic_folder = os.getcwd()+"\Bilder_opencv"                      ####How can I open pics from an other folder
    # files = os.listdir(pic_folder)
    image_files = glob.glob("*.jpg")
    for file in image_files:
        img_bgr = cv2.imread(file, cv2.IMREAD_COLOR)
        b, g, r = cv2.split(img_bgr)
        img_rgb = cv2.merge([r, g, b])
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.05, minNeighbors=6)

        print("number of recognized faces:", len(faces))

        for (x, y, w, h) in faces:
            cv2.rectangle(img_rgb, (x, y), (x + w, y + h), COLOR_FACE, 2)

        plt.axis('on')  # Diagramm-Achsen ausblenden
        plt.imshow(img_rgb)  # Dem Diagramm das Bild hinzufügen
        plt.title(file)  # Titel des Diagramms setzen
        plt.show()  # Diagramm anzeigen

   def face_EyesRecognition(self, folder):

    """ input: folder with *.jpg data
    output:
    - count of recognized faces
    - image with framed faces """

    COLOR_FACE = (255, 0, 255)
    COLOR_EYES = (0, 255, 0)
    # Bildordner bestimmen und Dateien auslesen
    # pic_folder = os.getcwd()+"\Bilder_opencv"                      ####How can I open pics from an other folder
    # files = os.listdir(pic_folder)
    image_files = glob.glob("*.jpg")
    for file in image_files:
        img_bgr = cv2.imread(file, cv2.IMREAD_COLOR)
        b, g, r = cv2.split(img_bgr)
        img_rgb = cv2.merge([r, g, b])
        img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
        faces = face_cascade.detectMultiScale(img_gray, scaleFactor=1.05, minNeighbors=6)

        print("number of recognized faces:", len(faces))

        for (x, y, w, h) in faces:
            cv2.rectangle(img_rgb, (x, y), (x + w, y + h), COLOR_FACE, 2)
            roi_gray = img_gray[y:y - int((y + h) * 0.7), x:x + w]
            roi_color = img_rgb[y:y - int((y + h) * 0.7), x:x + w]

            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), COLOR_EYES, 2)

                cv2.imshow('img', roi_color, img_gray)
        plt.axis('on')  # Diagramm-Achsen ausblenden
        plt.imshow(roi_color)  # Dem Diagramm das Bild hinzufügen
        plt.title(file)  # Titel des Diagramms setzen
        plt.show()  # Diagramm anzeigen


face_EyesRecognition("test.jpg")
