from flask import Flask, request, render_template, url_for, jsonify, Response
import cv2
import mediapipe as mp
 
from camera import Camera

app = Flask(__name__, template_folder='app/templates',static_folder="app/static")
camera = cv2.VideoCapture(0)
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# generate the image
def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

#def recognize_face():

def draw_rentangle():
    cv2.drawRentangle()

@app.route('/')
def testing():
    return 'hello world'

@app.route('/index')
def index():
    return render_template('page/index.html')

@app.route('/simple')
def simple():
    return jsonify(message = 'Hello from the Planetary API.')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message = "Sorry" + name + ", you are not old enough.")
    else:
        return jsonify(message="Welcome "+ name + ", you are old enough!")



@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/error.html', ErrorStatus=404),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/error.html', ErrorStatus=500),500    

if __name__ == "__main__":
    app.run(debug=True)