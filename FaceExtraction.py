"USAGE OF FACE DETECTION CLASS"


import cv2
import numpy as np
import face_recognition
from CFACE import Face_Detection



cap = cv2.VideoCapture(0)
fd = Face_Detection()

while True:
    success,imgs=cap.read()
   

   
    result = fd.detect_face(imgs)
    

    if result is not False:
        print(result)
        name = result[0][0]
        y1,x2,y2,x1= result[0][1]
        print (y1)
        print(x2)
        print (y2)
        print(x1)
        y1, x2, y2, x1 =y1*3, x2*5, y2*5, x1*4
        cv2.rectangle(imgs, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.rectangle(imgs, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
        cv2.putText(imgs,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
        
    

    cv2.imshow('webcam',imgs)
    cv2.waitKey(1)
