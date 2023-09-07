# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 18:15:58 2023

@author: visha
"""

import os
import cv2 as cv
import numpy as np

p = []

for i in os.listdir(r'D:\Projects\jasmcaus opencv-course master Resources\Faces\train'):
    print(i)
    p.append(i)
    
print(p)

DIR = r'D:\Projects\jasmcaus opencv-course master Resources\Faces\train'
haar_cascade = cv.CascadeClassifier('D:/Projects/haarcascade_frontalface_default.xml')


features = []
labels = []

# people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
def create_train():
    for person in p:
        path = os.path.join(DIR,person)
        label = p.index(person)
        
        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            
            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor =1.1 , minNeighbors = 4)
            
            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)
                # cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            
create_train()

print('Training Done.....')
features = np.array(features,dtype = object)
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

##Train the recogniozer on the features list and labels list

face_recognizer.train(features, labels)  

face_recognizer.save('face_trained.yml')              
np.save('features.npy',features)
np.save('labels.npy',labels)