import os
from flask import render_template, request, redirect
from app import app
from werkzeug.utils import secure_filename

from app.faceRec.faceRecognition7 import faceDetection
import cv2 as cv
from PIL import Image

filename="img/ayla.jpg"

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
    filepath = filename.split("/")[-1:][0]
    print(os.path.join(app.config["IMAGE_UPLOADS"])+"/ayla.jpg")
    img = cv.imread(os.path.join(app.config["IMAGE_UPLOADS"])+"/ayla.jpg", 0)

    cv.imwrite(os.path.join(app.config["IMAGE_UPLOADS"])+"/result.jpg", img)


    #faceDetection(filepath)

    #print(output)
    #new_filename = output
    new_filename = filename

    return render_template('edit_image.html', title='Editor', filename=filename, new_filename=new_filename)


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

                #print(os.path.join(app.config["IMAGE_UPLOADS"]))

                filename = "img/"+filename

                new_filename = "img/"+secure_filename(image.filename)

                # print(new_filename)
                # print(filename)

                return render_template('edit_image.html', title='Editor', filename=filename, new_filename=new_filename)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("upload_image.html", title='Upload')

