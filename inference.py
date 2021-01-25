import argparse
import cv2

from flask import Flask, render_template, Response
from datetime import datetime
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


def generate(cctv):
    start_time = time.time()
    time_thershold = 1  # second
    counter = 0
    fps_var = 0

    cap = cv2.VideoCapture(cctv)
    while True:
        ret, frame = cap.read()
        if ret:
            h_img, w_img, d_img = frame.shape
            now = datetime.now()
            now = '{}'.format(now.strftime("%d-%m-%Y %H:%M:%S"))

            counter += 1
            if (time.time() - start_time) > time_thershold:
                fps_var = counter / (time.time() - start_time)
                fps_var = int(fps_var)
                counter = 0
                start_time = time.time()

            info_frame = [
                ("FPS", fps_var),
                ("Date", now)
            ]

            x_text = 0
            y_text = h_img
            for (i1, (k, v)) in enumerate(info_frame):
                text = "{}: {}".format(k, v)
                cv2.putText(frame, text, (int(x_text), int(y_text) - ((i1 * 20) + 20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

            frame = cv2.imencode('.jpg', frame)[1].tobytes()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        else:
            print('no image')


@app.route('/video_feed')
def video_feed():
    return Response(generate(opt.source),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=str, default='/dev/video0', help='path to input source') # input file/folder, 0 for webcam
    opt = parser.parse_args()

    app.run(host="0.0.0.0", port=5000, threaded=True)
    # python3 inference.py --source /dev/video0