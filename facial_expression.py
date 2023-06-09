import cv2
from deepface import DeepFace as dff
import json

class facialExper():
    def __init__(self) -> None:
        self.module_path = 'haarcascade_frontalface_default.xml'
        self.face = cv2.CascadeClassifier(self.module_path)
        pass

    def detectExpr(self, frame):
        self.frame = frame
        self.imgGray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        faces = self.face.detectMultiScale(self.imgGray, minSize=(30, 30))
        emotions = ""

        for (x, y, w, h) in faces:
            faces = self.frame[y:y+h, x:x+w]
            outputs = ['emotion']
            result = dff.analyze(faces, actions=outputs, enforce_detection=False)
            emotions = result[0]['dominant_emotion']
        return emotions


def main():
    fe = facialExper()

    vidcap = cv2.VideoCapture(0)
    while vidcap.isOpened():
        ret, frame = vidcap.read()
        emo = fe.detectExpr(frame)#imgpath here
        print(emo)
    else:
        print("Cannot open camera")
if __name__ == "__main__":
    main()
