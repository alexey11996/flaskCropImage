from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image
import os
import glob
import shutil
import scripts
import time
import cairosvg

app = Flask(__name__)

photos = UploadSet("photos", IMAGES)

app.config["UPLOADED_PHOTOS_DEST"] = "static/init"
app.config["UPLOADED_PHOTOS_ALLOW"] = set(["png", "jpg", "jpeg", "svg"])
configure_uploads(app, photos)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST" and "photo" in request.files:
        filename = photos.save(request.files["photo"])
        print(filename)
        if ".svg" in filename:
            cairosvg.svg2png(
                url="./static/init/" + filename,
                write_to="./static/init/svg_" + filename.split(".svg")[0] + ".png",
            )
            os.remove("./static/init/" + filename)
            return render_template(
                "home.html",
                filename="/static/init/svg_%s" % (filename.split(".svg")[0] + ".png"),
            )
        elif ".svg" not in filename:
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
                if "svg_" in filename:
                    scripts.colorChange_SVG("." + filename, p, 0.3)
                else:
                    scripts.colorChange("." + filename, p, 0.3)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    elif option == "bright":
        for p in pr:
            if p != "":
                if "svg_" in filename:
                    scripts.colorChange_SVG("." + filename, p, 1.8)
                else:
                    scripts.colorChange("." + filename, p, 1.8)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    elif option == "neg":
        for p in pr:
            if p != "":
                if "svg_" in filename:
                    scripts.negative_SVG("." + filename, p)
                else:
                    scripts.negative("." + filename, p)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    elif option == "gs":
        for p in pr:
            if p != "":
                if "svg_" in filename:
                    scripts.gray_scale_SVG("." + filename, p)
                else:
                    scripts.gray_scale("." + filename, p)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    elif option == "sp":
        for p in pr:
            if p != "":
                if "svg_" in filename:
                    scripts.sepia_SVG("." + filename, p)
                else:
                    scripts.sepia("." + filename, p)
        newName = (
            "./static/init/" + str(time.time()) + filename.split("static/init/")[1]
        )
        os.rename("." + filename, newName)
        return render_template("croped.html", filename=newName)
    else:
        return render_template("croped.html", filename=filename)


if __name__ == "__main__":
    app.run(debug=True)
