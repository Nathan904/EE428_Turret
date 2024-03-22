import cv2
import numpy as np
import sys
from adafruit_servokit import ServoKit
import board
from adafruit_motorkit import MotorKit
import time


    
# Stepper Motor Initialization
#kit = MotorKit(i2c=board.I2C())
#kit.stepper1.onestep()
    
# Servos initialization
servohat = ServoKit(channels=16)
servoTilt = servohat.servo[8]
servoTrigger = servohat.servo[9]
servoTrigger.actuation_range = 270
#initial angles servos should be at
servoTrigger.angle = 45
servoTilt.angle = 90


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
connstr = 'libcamerasrc ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! videoscale ! clockoverlay time-format="%D %H:%M:%S" ! appsink'
cap = cv2.VideoCapture(connstr, cv2.CAP_GSTREAMER)

if cap.isOpened() == False:
    print('camera open Failed')
    sys.exit(0)

def imUpdate():
    success, img = cap.read() # Update Image
    if success == False:
        print('camera read Failed')
        sys.exit(0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:#may not work with parenthesese indexing *********
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)

#initMotors()
xalign = False
xcent = 240
ycent = 320
while True:
    yalign = True
    success, img = cap.read() # Update Image
    if success == False:
        print('camera read Failed')
        sys.exit(0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:#may not work with parenthesese indexing *********
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('img', img)
    while xalign == False:
        # Draw the rectangle around each face
        imUpdate()
        for (x, y, w, h) in faces:#may not work with parenthesese indexing *********
            imUpdate()
            xface = x+w/2#get updated x position of center of face
            if xface-10 < xcent <= xface+10:
                #target is aligned
                xalign = True
            elif xface < xcent:
                servoTilt.angle = servoTilt.angle - 1
                #NOTE: tilt servo has 0 as straight up and 180 as down
                #%tilt servo(current angle)
            elif xface > xcent:
                servoTilt.angle = servoTilt.angle + 1
                #%tilt servo(current angle)
        
    # while yalign == False:
        # success, img = cap.read()
        # if success == False:
            # print('camera read Failed')
            # sys.exit(0)

        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
        # faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        # # Draw the rectangle around each face
        # for (x, y, w, h) in faces:#may not work with parenthesese indexing *********
            # cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # yface =  y + h/2 #get updated y position of face
            # if yface-10 < ycent <= yface+10:
                # #target is aligned
                # yalign = True
            # elif yface < ycent:
                # #stepper reverse
                # kit.stepper1.onestep(direction=stepper.BACKWARD)
                # #stepper one step
            # elif yface > ycent:
                # #stepper forward
                # kit.stepper1.onestep(direction=stepper.FORWARD)
                # #stepper onestep
       
    if xalign == True and yalign == True:
        imUpdate()
        servoTrigger.angle = 80
        time.sleep(0.5)
        servoTrigger.angle = 45
        xalign = False
        #yalign = False
        
    # Display
    imUpdate()
    # Stop if escape key is pressed
    k = cv2.waitKey(30) & 0xff
    if k==27:
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()

