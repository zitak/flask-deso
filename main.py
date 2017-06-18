from flask import Flask, render_template, request
import functionality.index
from PIL import Image

ALLOWED_EXTENSIONS = set(['png', 'jpg'])

app = Flask(__name__)


def allowed_file(name):
    return '.' in name and name.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload():

    image = request.files['image']
    operation = request.form['operation']

    if image and allowed_file(image.filename) and operation:
        new_image = functionality.index.index(image, operation)
        return render_template('index.html')
    return render_template('index.html')


# @app.route('/')
# def download(image):


if __name__ == '__main__':
    app.run()
