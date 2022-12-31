from flask import Flask, request, render_template, url_for, jsonify, Response, redirect
import cv2
#import mediapipe as 
import matplotlib.pyplot as py
import time
import json

facexml = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_alt.xml')
eyexml = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")


#basic setting
app = Flask(__name__, template_folder='app/templates',static_folder="app/static")
camera = cv2.VideoCapture(0,cv2.CAP_DSHOW)
camera.set(3,640)
camera.set(4,480)
camera.set(10,100)
fps = camera.get(cv2.CAP_PROP_FPS)

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
            smaller_frame = cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
            rgb_small_frame = smaller_frame[:,:,::-1]
            gray = cv2.cvtColor(smaller_frame,cv2.COLOR_BGR2GRAY)
            faces = facexml.detectMultiScale(gray,1.3,5)
            eyes = eyexml.detectMultiScale(gray,1.3,5)
            fontScale = 1
            fontStyle = cv2.FONT_HERSHEY_COMPLEX_SMALL
            ntime = time.time()
            ptime = 0

            fps = 1/(ntime-ptime)
            ptime = ntime
            fps = int(fps)
            fps = str(fps)
            cv2.putText(gray, fps, (7, 70), fontStyle, 3, (100, 255, 0), 3, cv2.LINE_AA)

            for (x,y,w,h) in faces:
                cv2.rectangle(smaller_frame,(x,y),(x + w, y + h),(0,255,0),2)
                
                for (ex,ey,ew,eh) in eyes:
                    cv2.circle(smaller_frame,(ex+ew,ey+eh), 35,(255, 0, 0), 5)
                    cv2.putText(smaller_frame,'Eyes',(x + w, y + h),fontStyle,fontScale,(0,0,0),3,cv2.LINE_8)
                (flag,encodedImage) = cv2.imencode('.jpg', smaller_frame)    
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')
            

            
    


#detect multiple faces

#def ():


#Basic Routing
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

@app.route('/formtesting')
def formsetting():
    return render_template('page/formtesting.html')

@app.route('/success')
def success():
    return render_template('page/success.html')
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
# GET
# POST
@app.route('/formprocess', methods=['GET','POST'])
def formprocess():
    if request.method == 'POST':
        urls = {}
        urls[request.form['code']] = {'url': request.form['url']}
        with open('urls.json','w') as url_file:
             json.dump(urls, url_file)
        return render_template('page/success.html', code=request.form['code'])
    else:
        return redirect(url_for('index'))    
# PUT
# DELETE


#Error Response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('error/error.html', ErrorStatus=404),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('error/error.html', ErrorStatus=500),500    

if __name__ == "__main__":
    app.run(debug=True)