# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 16:18:03 2023

@author: visha
"""

from skimage.exposure import is_low_contrast
from imutils.paths import list_images
import argparse
import imutils
import cv2 as cv
import os 



cam = cv.VideoCapture(0)
cc = cv.VideoWriter_fourcc(*'XVID')
file = cv.VideoWriter('output.avi', cc, 15.0, (640, 480))
haar_cascade = cv.CascadeClassifier('D:/Projects/haarcascade_frontalface_default.xml')
if not cam.isOpened():
   print("error opening camera")
   exit()
while True:
   # Capture frame-by-frame
   ret, frame = cam.read()
   # if frame is read correctly ret is True
   if not ret:
      print("error in retrieving frame")
      break
   img = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
   gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
   blurred = cv.GaussianBlur(gray,(3,3), 0)
   edged = cv.Canny(blurred,30,150)
   faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

   text ="Low Contrast = NO"
   color = (0,255,0)

   if is_low_contrast(gray,fraction_threshold=0.45):
       text = "low Contrast = Yes"
       color = (0,0,255)
       
   else:
       cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
       cnts = imutils.grab_contours(cnts)
       c = max(cnts,key = cv.contourArea)
       
       cv.drawContours(img,[c], -1, (0,0,255),2)
       
       
       cv.putText(img, text, (5,25), cv.FONT_HERSHEY_SIMPLEX, 0.8,color, 2)
       for (x,y,w,h) in faces_rect:
           cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
           
       cv.imshow('detected faces',img)
       
       # show the output image and edge map
       cv.imshow("Image", img)
       cv.imshow("Edge", edged)
      # cv.imshow("blur", blurred)
  
   file.write(img)

   
   if cv.waitKey(1) == ord('q'):
      break

cam.release()
file.release()
cv.destroyAllWindows()




