
import time
import board
from adafruit_motorkit import MotorKit
from adafruit_servokit import ServoKit
from adafruit_motor import stepper

kit = MotorKit(i2c=board.I2C())
#Set number of channels for servo hat (should be 16  : 0-15 and we will use channels 15 and 14 for our two servos
servohat = ServoKit(channels=16)
tilt = servohat.servo[14]
trig = servohat.servo[15]
trig.actuation_range = 270
tilt.actuation_range = 180
tilt.angle = 90
trig.angle = 180
st = kit.stepper1
# want max steps to be 


