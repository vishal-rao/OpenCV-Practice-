# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 14:46:14 2023

@author: visha
"""

import cv2 as cv

img = cv.imread('D:/Projects/group.jpg')
img = cv.resize(img,(900,600))
# cv.imshow('person', img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

haar_cascade = cv.CascadeClassifier('D:/Projects/haarcascade_frontalface_default.xml')

faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    
cv.imshow('detected faces',img)

cv.waitKey(0)