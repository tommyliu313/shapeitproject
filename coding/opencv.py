#import items
import numpy as np
import cv2
from tkinter import *

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



#draw rectangle
def draw_rectangle():
    cv2.drawrectangle

#scenario 1: recognize people face
#process involved: face detection
#using function:  text
def puttext()
   text = cv2.putText(image, text,(80,80) ,cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,)

= cv2.

#class
#class object():

#basic definition
#    def __init__(name):
#        self.name = name




#window name
#視窗名稱,變數名稱
cv2.imshow("",)


