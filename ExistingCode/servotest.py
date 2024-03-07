import time
from adafruit_servokit import ServoKit


#Set number of channels for servo hat (should be 16  : 0-15 and we will use channels 15 and 14 for our two servos
servohat = ServoKit(channels=16)
tilt = servohat.servo[8]
trig = servohat.servo[9]
trig.actuation_range = 270

trig.angle = 45

tilt.angle = 90
time.sleep(3)
tilt.angle = 70
time.sleep(3)
tilt.angle = 110
time.sleep(1)
tilt.angle = 90

