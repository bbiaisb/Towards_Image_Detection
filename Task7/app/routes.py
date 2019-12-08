import os
import cv2 as cv
import shutil
from flask import render_template, request, redirect
from werkzeug.utils import secure_filename
from random import randint

from app import app

from app.functions.faceRecognition import face_detection
from app.functions.faceBlur import face_blur
from app.functions.eyeRecognition import faceRecognition_improve


app.config["IMAGE_UPLOADS"] = "Task7/app/static/img"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]


def allowed_image(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():

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
                error_msg = "Sorry, that file extension is not allowed."
                return render_template("upload_image.html", title='Upload', error=error_msg)

    return render_template("upload_image.html", title='Upload')


@app.route('/edit-image-face')
def edit_image_face():
    global filename, filename_new

    filepath = filename.split("/")[-1:][0]

    img = cv.imread(os.path.join(app.config["IMAGE_UPLOADS"])+"/"+filepath, 0)

    img = face_detection(img)

    cv.imwrite(os.path.join(app.config["IMAGE_UPLOADS"])+"/face_"+filepath, img)
    filename_new = "img/face_" + filepath

    filenames = [filename, filename_new]

    return render_template('edit_image.html', title='Editor', filename=filenames)


@app.route('/edit-image-blur')
def edit_image_blur():
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
    global filename, filename_new

    (filename_new, filename) = (filename, filename_new)

    filenames = [filename, filename_new]

    return render_template('edit_image.html', title='Editor', filename=filenames)


@app.route('/edit-image-eyes')
def edit_image_eyes():
    global filename, filename_new

    filepath = filename.split("/")[-1:][0]

    img = cv.imread(os.path.join(app.config["IMAGE_UPLOADS"]) + "/" + filepath, 0)

    img = faceRecognition_improve(img)

    cv.imwrite(os.path.join(app.config["IMAGE_UPLOADS"]) + "/eye_" + filepath, img)
    filename_new = "img/eye_" + filepath

    filenames = [filename, filename_new]

    print(filenames)

    return render_template('edit_image.html', title='Editor', filename=filenames)


@app.route('/edit-image-back')
def edit_image_back():
    global filename, filename_new, filename_initial
    filename = filename_initial
    filename_new = filename_initial

    filenames = [filename, filename_new]

    return render_template('edit_image.html', title='Editor', filename=filenames)
