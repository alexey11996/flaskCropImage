from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image
import os
import glob
import shutil

app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

app.config['UPLOADED_PHOTOS_DEST'] = 'static/init'
app.config['UPLOADED_PHOTOS_ALLOW'] = set(['png', 'jpg', 'jpeg'])
configure_uploads(app, photos)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return render_template('home.html', filename="/static/init/%s" % (filename))
    return render_template('home.html')


@app.route("/crop", methods=['POST'])
def crop():
    filename = request.form['filename']
    x1 = int(request.form['x1'])
    y1 = int(request.form['y1'])
    w = int(request.form['w'])
    h = int(request.form['h'])
    img = Image.open('.' + filename)
    area = (x1, y1, w + x1, h + y1)
    cropped_img = img.crop(area)
    cropped_img.save(filename.replace('/static/init/', 'static/cropped/'))
    return render_template('home.html')


@app.route("/croped")
def about():
    paths = glob.glob("static/cropped/*")
    n_paths = [w.replace('static/', '/static/') for w in paths]
    # print(n_paths)
    return render_template('croped.html', paths=paths)


@app.route("/delete")
def delete():
    files = glob.glob('static/cropped/*')
    for f in files:
        os.remove(f)
    return render_template('croped.html')


if __name__ == '__main__':
    app.run(debug=True)
