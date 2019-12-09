import os
import cv2 as cv
import shutil
from flask import render_template, request
from werkzeug.utils import secure_filename
from random import randint

from app import app
from app.functions.faceRecognition import face_detection
from app.functions.faceBlur import face_blur
# from app.functions.task3_faceRecognition import *
from app.functions.task4_measureSimilarities import measureSimilarities


app.config["IMAGE_UPLOADS"] = "Task7/app/static/img"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', title='404'), 404


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    """Display the uploaded image.

    If the upload form gets submitted with the "POST" method, check whether the
    provided file is valid, and if so delete all previously uploaded images, create
    a new filename and save the image to the "IMAGE_UPLOADS" path.
    """
    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if image.filename == "":
                error_msg = "Please provide a file for upload."
                return render_template("upload_image.html", title='Upload', error=error_msg)

            if allowed_image(image.filename):
                global filename, filename_new, filename_initial

                shutil.rmtree('Task7/app/static/img')
                os.makedirs('Task7/app/static/img')

                filename = str(randint(999, 10000))+"_"+secure_filename(image.filename)

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                filename = "img/"+filename
                filename_initial = filename[:]
                filename_new = filename
                filenames = [filename, filename_new]

                return render_template('edit_image.html', title='Editor', filename=filenames)

            else:
                error_msg = "Sorry, that file extension is not allowed. \n Try JPEG, JPG, PNG or GIF."
                return render_template("upload_image.html", title='Upload', error=error_msg)

    return render_template("upload_image.html", title='Upload')


@app.route('/edit-image-face')
def edit_image_face():
    """Apply face detection to the currently displayed image.

    Read the current image, on which the face_detection function imported from
    app/functions/faceRecognition.py needs to be applied. Then save that image
    with the prefix "face_" and display it.
    """
    global filename, filename_new

    filepath = filename.split("/")[-1:][0]
    img = cv.imread(os.path.join(app.config["IMAGE_UPLOADS"])+"/"+filepath, 0)

    img = face_detection(img)

    #image = Task3FaceDetection(img)

    #image.faceRecognition()

    cv.imwrite(os.path.join(app.config["IMAGE_UPLOADS"])+"/face_"+filepath, img)

    filename_new = "img/face_" + filepath
    filenames = [filename, filename_new]

    return render_template('edit_image.html', title='Editor', filename=filenames)


@app.route('/edit-image-blur')
def edit_image_blur():
    """Apply blurring to the currently displayed image.

    Read the current image, on which the face_blur function imported from
    app/functions/faceBlur.py needs to be applied. Then save that image
    with the prefix "blur_" and display it.
    """
    global filename, filename_new

    filepath = filename.split("/")[-1:][0]
    img = cv.imread(os.path.join(app.config["IMAGE_UPLOADS"])+"/"+filepath, 0)

    img = face_blur(img)

    cv.imwrite(os.path.join(app.config["IMAGE_UPLOADS"])+"/blur_"+filepath, img)
    filename_new = "img/blur_"+filepath
    filenames = [filename, filename_new]

    return render_template('edit_image.html', title='Editor', filename=filenames)


@app.route('/edit-image-swap')
def edit_image_swap():
    """Swap the two currently displayed images."""
    global filename, filename_new

    (filename_new, filename) = (filename, filename_new)
    filenames = [filename, filename_new]

    return render_template('edit_image.html', title='Editor', filename=filenames)


@app.route('/edit-image-eyes')
def edit_image_eyes():
    global filename, filename_new

    filepath = filename.split("/")[-1:][0]

    img = cv.imread(os.path.join(app.config["IMAGE_UPLOADS"]) + "/" + filepath, 0)

    #img = faceRecognition_improve(img)

    cv.imwrite(os.path.join(app.config["IMAGE_UPLOADS"]) + "/eye_" + filepath, img)
    filename_new = "img/eye_" + filepath

    filenames = [filename, filename_new]

    print(filenames)

    return render_template('edit_image.html', title='Editor', filename=filenames)


@app.route('/edit-image-similarities')
def edit_image_similarities():
    global filename, filename_new

    filepath = filename.split("/")[-1:][0]
    filepath_new = filename_new.split("/")[-1:][0]

    before = cv.imread(os.path.join(app.config["IMAGE_UPLOADS"]) + "/" + filepath, 0)
    after = cv.imread(os.path.join(app.config["IMAGE_UPLOADS"]) + "/" + filepath_new, 0)

    output = "The similarity score is: " + measureSimilarities(before, after)

    filenames = [filename, filename_new]

    return render_template('edit_image.html', title='Editor', filename=filenames, score_text=output)


@app.route('/edit-image-back')
def edit_image_back():
    """Reset the image to the initially uploaded image.

    Get and display the gobal variable filename_initial that has been set during the upload.
    """
    global filename, filename_new, filename_initial

    filename = filename_initial
    filename_new = filename_initial
    filenames = [filename, filename_new]

    return render_template('edit_image.html', title='Editor', filename=filenames)


def allowed_image(filename):
    """Check if the user uploads a valid image.

    The provided file should have an extension that is in the
    defined ALLOWED_IMAGE_EXTENSIONS list.
    """
    if "." not in filename:
        return False

    ext = filename.rsplit(".", 1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False
