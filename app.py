from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image
import os
import glob
import shutil
import scripts
import time

app = Flask(__name__)


# @app.after_request
# def after_request_callback(response):
#     files = glob.glob('static/init/*')
#     for f in files:
#         os.remove(f)
#     return response


photos = UploadSet("photos", IMAGES)

app.config["UPLOADED_PHOTOS_DEST"] = "static/init"
app.config["UPLOADED_PHOTOS_ALLOW"] = set(["png", "jpg", "jpeg"])
configure_uploads(app, photos)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" and "photo" in request.files:
        filename = photos.save(request.files["photo"])
        return render_template("home.html", filename="/static/init/%s" % (filename))
    return render_template("home.html")


@app.route("/crop", methods=["POST"])
def crop():
    option = request.form["option"]
    filename = request.form["filename"]
    params = request.form["params"]
    pr = params.split("&")
    if option == "dark":
        for p in pr:
            if p != "":
                scripts.colorChange("." + filename, p, 0.3)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    elif option == "bright":
        for p in pr:
            if p != "":
                scripts.colorChange("." + filename, p, 1.8)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    elif option == "neg":
        for p in pr:
            if p != "":
                scripts.negative("." + filename, p)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    elif option == "wb":
        for p in pr:
            if p != "":
                scripts.white_black("." + filename, p, 0.8)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    elif option == "gs":
        for p in pr:
            if p != "":
                scripts.gray_scale("." + filename, p)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    elif option == "sp":
        for p in pr:
            if p != "":
                scripts.sepia("." + filename, p)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    else:
        return render_template("croped.html", filename=filename)


# @app.route("/croped")
# def about():
#     paths = glob.glob("static/cropped/*")
#     n_paths = [w.replace('static/', '/static/') for w in paths]
#     # print(n_paths)
#     return render_template('croped.html', paths=paths)


# @app.route("/delete")
# def delete():
#     files = glob.glob('static/cropped/*')
#     for f in files:
#         os.remove(f)
#     return render_template('croped.html')


if __name__ == "__main__":
    app.run(debug=True)
