from flask import Flask, render_template, request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from PIL import Image, ImageFilter
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
    params = request.form['params']
    pr = params.split("&")
    for p in pr:
        if (p != ''):
            scripts.bright('.' + filename, p, 0.4)
    print(filename)
    newName = './static/init/' + \
        str(time.time()) + filename.split('static/init/')[1]
    os.rename('.' + filename, newName)

    return render_template('croped.html', filename=newName)
    print(123)

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


if __name__ == '__main__':
    app.run(debug=True)

# box = (30, 30, 110, 110)
# ic = image.crop(box)
# for i in range(10):  # with the BLUR filter, you can blur a few times to get the effect you're seeking
#     ic = ic.filter(ImageFilter.BLUR)
# image.paste(ic, box)

    # filename = request.form['filename']
    # x1 = int(request.form['x1'])
    # y1 = int(request.form['y1'])
    # w = int(request.form['w'])
    # h = int(request.form['h'])
    # img = Image.open('.' + filename)
    # area = (x1, y1, w + x1, h + y1)
    # cropped_img = img.crop(area)
    # cropped_img.save(filename.replace('/static/init/', 'static/cropped/'))
    # return render_template('home.html')
