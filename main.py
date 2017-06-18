from flask import Flask, render_template, request, send_file
import functionality.index
from io import BytesIO

ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__)


def allowed_file(name):
    return '.' in name and name.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/', methods=['GET','POST'])
def upload():

    image = request.files['image']
    form = request.form
    operation = form['operation']

    if image and allowed_file(image.filename) and operation:
        new_image = functionality.index.index(image, operation)
        if 'download' in form:
            img_io = BytesIO()
            new_image.save(img_io, 'JPEG')
            img_io.seek(0)
            #TODO new name and extension
            return send_file(img_io, mimetype='image/jpeg', as_attachment=True, attachment_filename='new.jpg')
        elif 'preview' in form:
            #TODO
            print("preview")
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
