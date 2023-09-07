# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 16:44:00 2023

@author: visha
"""

import numpy as np 
import cv2 as cv

haar_cascade = cv.CascadeClassifier('D:/Projects/haarcascade_frontalface_default.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'D:\Projects\jasmcaus opencv-course master Resources\Faces\val\madonna\3.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person',gray)

##detect face

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

for(x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+h]
    
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')
    
    cv.putText(img, str(people[label]), (20,20),cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0))
    cv.rectangle(img, (x,y),(x+w,y+h),(0,255,0),thickness = 2)

cv.imshow('Detectd face', img)
cv.waitKey(0)
    


