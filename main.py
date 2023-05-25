from eye_gaze import eyeGaze
from facial_expression import facialExper
from csvcrud import ccrud
import cv2

def main():
    ct = 1
    eg = eyeGaze()
    fe = facialExper()
    egfe = ccrud()
    field = ["id", "emotion", "gaze"]
    egfe.createFile("gazeEmo.csv", field)
    vidcap = cv2.VideoCapture(0)
    while vidcap.isOpened():
        ret, frame = vidcap.read()
        pos = eg.detect_Gaze(frame)
        emo = fe.detectExpr(frame)
        print("emotion, position: ", emo + "," + pos)
        egfe.writeRow("gazeEmo.csv", [str(ct), emo, pos])
        ct+=1
    else:
        print("Cannot open camera")


if __name__=="__main__":
    main()