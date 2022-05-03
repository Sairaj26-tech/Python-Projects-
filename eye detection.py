

import numpy as np
import cv2
eye_cascade = cv2.CascadeClassifier("C:/Users/Swaroopgowda/Desktop/eyedetector/myproject/haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
id=input("Enter user id")
sampleN=0;
while 1:
    ret,img=cap.read()
    print("pixel of rgb",img)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    print("pixel of gray",gray)
    eyes=eye_cascade.detectMultiScale(gray,1.3,5)
    print(eyes)
    for(x,y,w,h) in eyes:
        sampleN=sampleN+1
        cv2.imwrite("C:/Users/Swaroopgowda/Desktop/eyedetector/myproject/dataset1/user."+str(id)+"."+str(sampleN)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.rectangle(roi_color,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
        cv2.imshow("image",img)
    if(sampleN>100):
        break
cap.release()
cv2.destroyAllWindows()

import numpy as np
import cv2
eye_cascade = cv2.CascadeClassifier("C:/Users/Swaroopgowda/Desktop/eyedetector/myproject/haarcascade_eye.xml")

cap = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("C:/Users/Swaroopgowda/Desktop/eyedetector/myproject/trainingdata.yml")

id=0

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    eyes = eye_cascade.detectMultiScale(gray, 1.5, 5)
    for (x,y,w,h) in eyes:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        
        if(id==12):
            print("chandana")
        elif(id==10):
            print("suma")
        elif(id==13):
            print("manju")
        
    cv2.imshow('img',img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
import os
import numpy as np
import cv2

from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()

path="C:/Users/Swaroopgowda/Desktop/eyedetector/myproject/dataset1/"


def getImagesWithID(path):

    imagePaths = [os.path.join(path, f) for f in os.listdir(path)]   

    eyes = []

    IDs = []

    for imagePath in imagePaths:      


        eyesImg = Image.open(imagePath).convert('L')

        eyeNP = np.array(eyesImg, 'uint8')



        ID= int(os.path.split(imagePath)[-1].split(".")[1])


        eyes.append(eyeNP)
        IDs.append(ID)
        cv2.imshow("Adding faces for traning",eyeNP)
        cv2.waitKey(10)

    return np.array(IDs), eyes

Ids,eyes  = getImagesWithID(path)
recognizer.train(eyes,Ids)

recognizer.save("C:/Users/Swaroopgowda/Desktop/eyedetector/myproject/trainingdata.yml")

cv2.destroyAllWindows()

