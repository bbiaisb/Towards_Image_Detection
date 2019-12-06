import os
from flask import render_template, request, redirect
from app import app
from werkzeug.utils import secure_filename
from random import randint


from app.faceRec.faceRecognition import face_detection
import cv2 as cv
from PIL import Image

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
                print("No filename")
                return redirect(request.url)

            if allowed_image(image.filename):
                global filename

                filename = str(randint(999, 10000))+secure_filename(image.filename)

                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

                filename = "img/"+filename
                filenames = [filename, filename[:]]

                print(filenames)

                return render_template('edit_image.html', title='Editor', filename=filenames)

            else:
                print("That file extension is not allowed")
                return redirect(request.url)

    return render_template("upload_image.html", title='Upload')


@app.route('/edit-image')
def edit_image():
    try:
        if num > 1:
            num += 0
    except:
        num = 1

    print("Oh dear"+filename)

    filepath = filename.split("/")[-1:][0]

    img = cv.imread(os.path.join(app.config["IMAGE_UPLOADS"])+"/"+filepath, 0)

    img = face_detection(img)

    cv.imwrite(os.path.join(app.config["IMAGE_UPLOADS"])+"/"+str(num)+".jpg", img)

    new_filename = "img/"+str(num)+".jpg"
    num += 1

    filenames = [filename[:], new_filename[:]]
    print(filenames)

    return render_template('edit_image_face.html', title='Editor', filename=filenames[:])

