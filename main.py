from flask import Flask, render_template, request, send_file
import functionality.index
from io import BytesIO

ALLOWED_EXTENSIONS = ['png', 'jpg']

app = Flask(__name__)


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def upload():

    image = request.files['image']
    filename = image.filename.rsplit('.', 2)
    name = filename[0]
    extension = filename[1]
    if extension == 'jpg':
        ext = 'JPEG'
    else:
        ext = extension.upper()

    form = request.form
    operation = form['operation']

    if image and extension in ALLOWED_EXTENSIONS and operation:
        new_image = functionality.index.index(image, operation)
        if 'download' in form:
            img_io = BytesIO()
            new_image.save(img_io, ext)
            img_io.seek(0)
            new_name = name + '_' + operation + '.' + extension
            return send_file(img_io, mimetype='image', as_attachment=True, attachment_filename=new_name)
        if 'preview' in form:
            new_image.show()
            # TODO save values from form
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
