import cv2
import numpy as np
import sys
import time
from adafruit_servokit import ServoKit
import board
from adafruit_motorkit import MotorKit

#Initialize Stepper Motor
kit = MotorKit(i2c=board.I2C())
kit.stepper1.onestep()
#time.sleep(0.01)
#kit.stepper1.release() #Release afer motion to allow freespin 

#Servos initialization
#Set number of channels for servo hat (should be 16  : 0-15 and we will use channels 15 and 14 for our two servos
servohat = ServoKit(channels=16)
tilt = servohat.servo[8]
trig = servohat.servo[9]
trig.actuation_range = 270
#initial angles servos should be at
trig.angle = 45
tilt.angle = 90
currtilt = 90;

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
connstr = 'libcamerasrc ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! videoscale ! clockoverlay time-format="%D %H:%M:%S" ! appsink'
cap = cv2.VideoCapture(connstr, cv2.CAP_GSTREAMER)

if cap.isOpened() == False:
    print('camera open Failed')
    sys.exit(0)


while True:

    succes, img = cap.read()
    if succes == False:
        print('camera read Failed')
        sys.exit(0)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
    #elif k==ord('M'):
        #cv2.putText(img,'Manual Mode', (10,10), cv2.FONT_HERSHEY_SIMPLEX, 1,(0,255,0), 2)
        #cv2.imshow('img', img)
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()

def fireturret(mode):
    if(mode == 'semi'):
        trig.angle = 65
        time.sleep(0.1)
        trig.angle = 45
    elif(mode == 'burst'):
        trig.angle = 65
        time.sleep(0.6)
        trig.angle = 45
    elif(mode == 'auto'):
        trig.angle = 65
        time.sleep(1)
        trig.angle = 45
    