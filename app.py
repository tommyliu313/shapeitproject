from flask import Flask, request, render_template, url_for, jsonify, Response
import cv2
#import mediapipe as 
import matplotlib.pyplot as py
 
facexml = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
eyexml = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


#basic setting
app = Flask(__name__, template_folder='app/templates',static_folder="app/static")
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
#mp_face_detection = mp.solutions.face_detection
#mp_drawing = mp.solutions.drawing_utils

#variables
#font = ""
#size = ""

# generate the image
def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            if ret:
                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                faces = facexml.detectMultiScale(gray,1.3,5)
                eyes = eyexml.detectMultiScale(gray,1.3,5)
                fontScale = 1
                fontStyle = cv2.FONT_HERSHEY_COMPLEX_SMALL
                for (x,y,w,h) in faces:
                    cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0))
                    cv2.putText(frame,'Person',(x + w, y + h),fontStyle,fontScale,(0,0,0),3,cv2.LINE_8)
                    for (ex,ey,ew,eh) in eyes:
                        cv2.circle(frame,(ex+ew,ey+eh), 35,(255, 0, 0), 5)
                        cv2.putText(frame,'Eyes',(x + w, y + h),fontStyle,fontScale,(0,0,0),3,cv2.LINE_8)
                
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            

            
    


#detect multiple faces

#def ():


#Basic Routing
@app.route('/')
def testing():
    return 'hello world'

@app.route('/index')
def index():
    return render_template('page/index.html')

@app.route('/simple')
def simple():
    return jsonify(message = 'Hello from the Planetary API.')

@app.route('/visualize')
def visualize():
    return render_template('page/visualizedata.html')

@app.route('/setting')
def setting():
    return render_template('page/setting.html')
    
#Video
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

#Testing
@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message = "Sorry" + name + ", you are not old enough.")
    else:
        return jsonify(message="Welcome "+ name + ", you are old enough!")

# CRUD Operation
#@app.route('', methods=['GET','POST'])
#def


#Error Response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/error.html', ErrorStatus=404),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/error.html', ErrorStatus=500),500    

if __name__ == "__main__":
    app.run(debug=True)