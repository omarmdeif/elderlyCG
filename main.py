from eye_gaze import eyeGaze
from facial_expression import facialExper 
import cv2

def main():
    eg = eyeGaze()
    fe = facialExper()
    vidcap = cv2.VideoCapture(0)
    while vidcap.isOpened():
        ret, frame = vidcap.read()
        pos = eg.detect_Gaze(frame)
        emo = fe.detectExpr(frame)
        print("emotion, position: ", emo + "," + pos)
    else:
        print("Cannot open camera")


if __name__=="__main__":
    main()