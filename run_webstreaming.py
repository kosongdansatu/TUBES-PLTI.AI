# main.py

from flask import Flask, render_template, Response
from streaming import run

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen():
    while True:
       # frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + run() + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    app.run(host='localhost', debug=True, port=5050)
