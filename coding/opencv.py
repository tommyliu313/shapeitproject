#import items
import numpy as np
import cv2

# setting
yellow = (255,255,0)
black = (0,0,0)
window_size = (1080,720,3)
text = "Testing"

#load images
image = cv2.imread("")

#background
white_screen = np.ones(window_size, np.uunt8)

# video
cap = cv2.videoCapture(0)

    
# convert color


# convert = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
human_face_template = cv2.cascadeClassifier("CascadeClassifier\haarcascade_frontalface_alt.xml");

if human_face_template.empty() == True:
    pass

#effects (thresholding) 


#class
class object():

#basic definition
    def __init__(name):
        self.name = name



#scenario 1: recognize people face
#process involved: face detection
#using function:  text

text = cv2.putText(image, text,(80,80) ,cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,)

= cv2.





#window name
#視窗名稱,變數名稱
cv2.imshow("",)

#Camera Setting

while(True):
# click the button esc and do the following action
    ret, frame = cap.read(1)
    if cv2.waitKey(1) & 0xFF == ord('esc'):
        break
# close the application

cv2.waitKey(0)
cv2.destroyAllWindows()

