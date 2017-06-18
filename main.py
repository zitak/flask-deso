from flask import Flask, render_template
import functionality.index


app = Flask(__name__)


@app.route('/')
def home():

    # path = "D:/Projects/flask-deso/images/balloons.jpg"
    # functionality.index.index(path)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
