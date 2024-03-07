import time
import adafruit_motorkit
import board
from adafruit_motorkit import MotorKit
from adafruit_servokit import ServoKit


def initMotors():
    
    # Stepper Motor Initialization
    kit = MotorKit(i2c=board.I2C())
    kit.stepper1.onestep()
    
    # Servos initialization
    servohat = ServoKit(channels=16)
    servoTilt = servohat.servo[8]
    servoTrigger = servohat.servo[9]
    servoTrigger.actuation_range = 270
    #initial angles servos should be at
    servoTrigger.angle = 45
    servoTilt.angle = 90
    
    



#Servos initialization
#Set number of channels for servo hat (should be 16  : 0-15 and we will use channels 15 and 14 for our two servos

currtilt = 9
