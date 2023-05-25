import os
import cv2
import face_recognition
import numpy as np
class Face_Detection:
    def __init__(self) -> None:
        self.saved_faces=[]
        self.classNames=[]

        self.init_faces('faces')



        
    def init_faces(self,path):
        images=[]
        images_path=os.listdir(path)
        
        for cls in images_path:
            img=cv2.imread(f'{path}/{cls}')
            images.append(img)
            self.classNames.append(os.path.splitext(cls)[0])
        self.saved_faces = self.findencodeing(images=images)
    
    def findencodeing(self,images):
        encodelist=[]
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode=face_recognition.face_encodings(img)[0]
            encodelist.append(encode)
        return encodelist
    def detect_face(self,img):
        "returns a 2d list consisting of [label,[x1,y1,x2,y2]]"
        img=cv2.resize(img,(0,0),None,0.25,0.25)
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        faceCurrFrame=face_recognition.face_locations(img)
        encodeCurrFrame = face_recognition.face_encodings(img,faceCurrFrame)
        detected_faces = False
        for encodeFace,faceLoc in zip(encodeCurrFrame,faceCurrFrame):
            matches=face_recognition.compare_faces(self.saved_faces,encodeFace)
            faceDIS=face_recognition.face_distance(self.saved_faces,encodeFace)
            matchIndex=np.argmin(faceDIS)

            if matches[matchIndex]:
                detected_faces = []

                name=self.classNames[matchIndex].upper()
                detected_faces.append([name,faceLoc])

        return detected_faces
