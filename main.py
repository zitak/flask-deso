from flask import Flask
import functionality.index

app = Flask(__name__)


@app.route('/')
def main():
    path = "D:/Projects/flask-deso/images/balloons.jpg"
    functionality.index.index(path)
    return 'OK'


if __name__ == '__main__':
    app.run()
