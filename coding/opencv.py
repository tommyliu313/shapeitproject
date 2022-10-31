#import items
import numpy as np
import cv2


#load images
image = cv2.imread("")
#cla

# video
cap = cv2.videoCapture(0)

while(true):
    
# convert color

convert = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
human_face_template = cv2.cascadeClassifier("CascadeClassifier\haarcascade_frontalface_alt.xml");


#class
class object():

#basic definition
    def __init__(name):
        self.name = name



#effects (thresholding)

#window name
#視窗名稱,變數名稱
cv2.imshow("",)



# click the button esc and do the following action
if cv2.waitKey(1) & 0xFF == ord('esc'):
    break
# close the application

cv2.waitKey(0)
cv2.destroyAllWindows()