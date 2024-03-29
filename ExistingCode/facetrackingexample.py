import numpy as np
import serial
import cv2

#arduino = serial.Serial(port="/dev/ttyACM0", baudrate=115200)
#reset_input_buffer()
#reset_output_buffer()

print("Connected to pi...")

face_cascade = cv2.CascadeClassifier('classifiers/haarcascade_frontalface_alt.xml')

print("Created classifiers...")
cap = cv2.VideoCapture(0)
print("Opened video feed...")

def set_res(cap, x,y):
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(x))
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, int(y))

frame_w = 640
frame_h = 480
set_res(cap, frame_w,frame_h)

while(True):
    ret, frame = cap.read()
    cap.read()
  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = np.array([]) 
    faces = face_cascade.detectMultiScale(
        gray,   
        scaleFactor=1.1,
    )
    
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    if ([i for i in faces]):
        face_center_x = faces[0,0]+faces[0,2]/2
        face_center_y = faces[0,1]+faces[0,3]/2

        err_x = 30*(face_center_x - frame_w/2)/(frame_w/2)
        err_y = 30*(face_center_y - frame_h/2)/(frame_h/2)
        

        if abs(err_x) < 3 and abs(err_y) < 3:
            data = "1000.0X0Y".format(err_x, err_y)
            print("shoot!")
            arduino.write(bytes(data, 'utf-8'))
        else:
            data = "{:.3f}X{:.3f}Y".format(err_x, err_y)
            print(data)
            arduino.write(bytes(data, 'utf-8'))

                     
arduino.close()
cap.release()
cv2.destroyAllWindows()