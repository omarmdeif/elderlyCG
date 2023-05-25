from eye_gaze import eyeGaze
from facial_expression import facialExper
from csvcrud import ccrud
import cv2
import numpy as np
import face_recognition
from CFACE import Face_Detection
from datetime import datetime

def main():
    ct = 1
    eg = eyeGaze()
    fe = facialExper()
    fd = Face_Detection()
    egfe = ccrud()
    field = ["id", "dateTime","emotion", "gaze", "faceName"]
    egfe.createFile("gazeEmo.csv", field)
    vidcap = cv2.VideoCapture(0)
    while vidcap.isOpened():
        ret, frame = vidcap.read()
        dt = datetime.now()
        pos = eg.detect_Gaze(frame)
        emo = fe.detectExpr(frame)
        det = fd.detect_face(frame)
        print("emotion, position: ", dt+","+emo + "," + pos + "," + det[0][0])
        egfe.writeRow("gazeEmo.csv", [str(ct), dt, emo, pos, det[0][0]])
        ct+=1

        cv2.imshow('webcam',frame)
        cv2.waitKey(1)
    else:
        print("Cannot open camera")


if __name__=="__main__":
    main()