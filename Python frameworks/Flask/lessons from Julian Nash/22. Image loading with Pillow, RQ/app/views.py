import os
import secrets

from flask import render_template, request, flash

from . import app, q
from .tasks import create_image_set

app.config["SECRET_KEY"] = "liruhfoi34uhfo8734yot8234h"
app.config[
    "UPLOAD_DIRECTORY"] = "/Users/ervand_agadzhanyan/Desktop/Summary/Flask/lessons from Julian Nash/22. Image loading with Pillow, RQ/app/static/img/uploads"


@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    message = None

    if request.method == "POST":
        image = request.files["image"]
        image_dir_name = secrets.token_hex(16)
        os.mkdir(os.path.join(app.config["UPLOAD_DIRECTORY"], image_dir_name))
        image.save(os.path.join(app.config["UPLOAD_DIRECTORY"], image_dir_name, image.filename))
        image_dir = os.path.join(app.config["UPLOAD_DIRECTORY"], image_dir_name)
        q.enqueue(create_image_set, image_dir, image.filename)
        flash("Image uploaded and sent for resizing", category="success")
        message = f"/image/{image_dir_name}/{image.filename.split('.')[0]}"

    return render_template("upload_image.j2", message=message)


@app.route("/image/<dir>/<img>")
def view_image(dir, img):
    return render_template("view_image.j2", dir=dir, img=img)
