import os
from flask import render_template, request, redirect
from app import app
from werkzeug.utils import secure_filename

from faceRecognition import faceDetection
import cv2 as cv
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


@app.route('/edit-image')
def edit_image():
    img = cv.imread(filename)
    output = faceDetection(img)
    # cv.imshow('img_2', output)
    return render_template('edit_image.html', title='Editor', filename=output)


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    global filename

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if image.filename == "":
                print("No filename")
                return redirect(request.url)

            if allowed_image(image.filename):
                filename = secure_filename(image.filename)

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                filename = "img/"+filename

                return render_template('edit_image.html', title='Editor', filename=filename)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("upload_image.html", title='Upload')
