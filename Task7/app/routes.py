import os
from flask import render_template, request, redirect
from app import app

app.config["IMAGE_UPLOADS"] = "Task7/app/upolads"

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Florian'}
    return render_template('index.html', title='Home', user=user)


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":

        if request.files:
            image = request.files["image"]

            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))

            print("Image saved")

            return redirect(request.url)

    return render_template("upload_image.html")
