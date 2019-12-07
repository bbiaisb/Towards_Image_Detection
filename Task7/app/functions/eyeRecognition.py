import cv2
from matplotlib import pyplot as plt
import numpy as np

def faceRecognition_improve(file):
    COLOR_FACE = (255, 0, 255)
    COLOR_EYES = (255, 0, 0)

    #img_bgr = cv2.imread(file, cv2.IMREAD_COLOR)
    #b, g, r = cv2.split(img_bgr)
    #img_rgb = cv2.merge([r, g, b])

    #img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
    faces = face_cascade.detectMultiScale(file, scaleFactor=1.05, minNeighbors=6)

    count_faces = 0
    # print("number of recognized faces:", len(eyes))

    for (x, y, w, h) in faces:
        cv2.rectangle(img_rgb, (x, y), (x + w, y + h), COLOR_FACE, 2)
        roi_gray = img_gray[y:y - int((y + h) * 0.9), x:x + w]
        roi_color = img_rgb[y:y - int((y + h) * 0.9), x:x + w]

        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), COLOR_EYES, 2)
            count_faces += len(eyes) // 2


    # plt.axis('on')  # Diagramm-Achsen ausblenden
    #plt.imshow(img_rgb)  # Dem Diagramm das Bild hinzufügen
    #plt.title(file)  # Titel des Diagramms setzen
    #plt.show()  # Diagramm anzeigen

    cv2.imshow("img", img_rgb)
    cv2.waitKey()
    cv2.destroyAllWindows()


    print("number of recognized faces:", count_faces)

    return faces


#print(faceRecognition_improve("closedeyes_1.jpg"))
