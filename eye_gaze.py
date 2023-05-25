import cv2
import mediapipe as mp
import math
import numpy as np
import csv


class eyeGaze():
    def __init__(self) -> None:
        self.FONTS = cv2.FONT_HERSHEY_COMPLEX
        self.map_face_mesh = mp.solutions.face_mesh
        self.RightEyeRight = [33]
        self.RightEyeLeft = [133]
        self.LeftEyeRight = [362]
        self.LeftEyeLeft = [263]
        self.LeftIris = [474,475,476,477]
        self.RightIris = [469,470,471,472]
        #self.lmposition = []
        self.flag,self.ctright,self.ctleft=0,0,0
        pass

    def detect_Gaze(self, frame):
        with self.map_face_mesh.FaceMesh(max_num_faces=1,refine_landmarks=True,min_detection_confidence=0.5,
                            min_tracking_confidence=0.5) as face_mesh:

            
                #  resizing frame
                frame = cv2.flip(frame,1)
                #frame_height, frame_width = frame.shape[:2]
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                results = face_mesh.process(rgb_frame)
                h,w,c = frame.shape
                if results.multi_face_landmarks:
                    facepoints =np.array([np.multiply([p.x,p.y],[w,h]).astype(int)
                                         for p in results.multi_face_landmarks[0].landmark])
                    (cx,cy),radiusl = cv2.minEnclosingCircle(facepoints[self.LeftIris])
                    (rx,ry), radiusr = cv2.minEnclosingCircle(facepoints[self.RightIris])
                    centerright = np.array([rx,ry],dtype=np.int32)
                    cv2.circle(frame,centerright,int(radiusl),(0,0,255),1,cv2.LINE_AA)
                    distanceHalf = np.linalg.norm(centerright - facepoints[self.RightEyeRight])
                    distanceAll = np.linalg.norm(facepoints[self.RightEyeLeft] - facepoints[self.RightEyeRight])
                    ratio = distanceHalf / distanceAll
                    if ratio <= 0.4:
                        position = 'right'
                        flag=1
                        self.ctright+=1
                    if ratio > 0.4 and ratio <= 0.6:
                        position= 'Center'
                        flag=1
                    if ratio > 0.6:
                        position = ' left'
                        flag=1
                        self.ctleft+=1
                    if flag!=1:
                        position = 'Eye closed'
                    flag = 0
                    return position
                    # with open(filename, 'a', newline='') as csvfile:
                    # # Create a writer object
                    #     writer = csv.writer(csvfile)

                    # # Append the value to the CSV file
                    #     writer.writerow([position])
                    #self.lmposition.append(position)
                # cv2.putText(frame,position,(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
                # key = cv2.waitKey(20)
                # if key == ord('q') or key == ord('Q'):
                #     break
        pass 


def main():
    eg = eyeGaze()
    vidcap = cv2.VideoCapture(0)
    while vidcap.isOpened():
        ret, frame = vidcap.read()
        pos = eg.detect_Gaze(frame)#imgpath here
        print(pos)
    else:
        print("Cannot open camera")


if __name__=="__main__":
    main()