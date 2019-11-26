import sys
import cv2
import numpy
class Image(object):

    def __init__(self, img_path):
        self.img = cv2.imread(img_path)

        # additional features which might be relevant to keep?

    def show(self):
        image = cv2.imshow('img', self.img)

        # return image

    def coordinates (self):
        return self.img

    # additional operations on your image objects?
class FaceDetectionBaseline(object):

    def __init__(self):
        self.classifier_face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.classifier_eyes = cv2.CascadeClassifier('haarcascade_eye.xml')

    def input_transform(self, input_image):

        pass

    def detect_face(self, input_image):

        """
        input: Image object
        output: list of coordinates for the face (x0, y0, width, height )
        """

        # makes pict
        gray = cv2.cvtColor(input_image.img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        faces = self.classifier_face.detectMultiScale(gray, 1.1, 4)
        return faces


    def detect_eyes(self, input_image):

        """
        input: Image object
        output: list of coordinates of eyes (x0, y0, width, height )
        """
        # makes pict
        gray = cv2.cvtColor(input_image.img, cv2.COLOR_BGR2GRAY)
        # Detect faces
        eyes = self.classifier_eyes.detectMultiScale(gray, 1.1, 4)
        return eyes


class BetterFaceDetection(FaceDetectionBaseline):

    def __init__(self):

# super().__init__()/
    def rectangle_faces(self, faces, input_image):
        for (x, y, w, h) in faces:
            cv2.rectangle(input_image.img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        input_image.show()
        cv2.waitKey()

    def rectangle_faces_and_eyes(self, faces, eyes, input_image):
        for (x, y, w, h) in faces:
            cv2.rectangle(input_image.img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = faces[y:y - int((y + h) * 0.7), x:x + w]
            roi_color = input_image[y:y - int((y + h) * 0.7), x:x + w]  # ROi just upper than 70%, so the mouth won't be considered as eye

            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        input_image.show()
        cv2.waitKey()

# class FoolSecurity(BetterFaceDetection):
#     def __int__(self):
#         # self.classifier_eyes
#
#     def black_eyes(self, eyes):                         #Idea: intensity reduce => Eye getting black
#         new_img = []
#         for (ex, ey, ew, eh) in eyes:
#             ex, ey, ew, eh += random.randient()
#

            #how can I calculate a hole matrix and append it as well.
            #shouldn't be a matrix any more -> gray!



def main(file_path):

    #load image
    input_image = Image(file_path)
    #initialise classifier
    classifier = FaceDetectionBaseline()

    # perform classification
    coordinates = classifier.detect_face(input_image)



    # plot result

    for (x, y, w, h) in coordinates:

        cv2.rectangle(input_image.img, (x, y), (x+w, y+h), (255, 0, 0), 2)



    input_image.show()

    cv2.waitKey()



# if __name__=='__main__':
#
#     file_path = sys.argv[1]
#
#     main(file_path)


#how can i call a function in a class
# all classes in one file or should I split?
#how can I get the coordinates
#how can I put extend tho image-> wrong path...


print(Image.coordinates("test.jpg"))