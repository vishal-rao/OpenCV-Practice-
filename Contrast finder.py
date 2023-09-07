# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 15:46:08 2023

@author: visha
"""

from skimage.exposure import is_low_contrast
from imutils.paths import list_images
import argparse
import imutils
import cv2 as cv
import os 

file_path  = r'D:\ML Datasets\Apples2Oranges.v1i.folder\train\stitch'
image = []
for i in os.listdir(file_path):
    img = os.path.join(file_path, i)
    
    image.append(img)
    
for i in image:
    print('processing image')
    image= cv.imread(i)
    image = imutils.resize(image,width=450)
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    blurred = cv.GaussianBlur(gray,(3,3), 0)
    edged = cv.Canny(blurred,30,150)
    
    text ="Low Contrast = NO"
    color = (0,255,0)
    
    if is_low_contrast(gray,fraction_threshold=0.35):
        text = "low Contrast = Yes"
        color = (0,0,255)
        
    else:
        cnts = cv.findContours(edged.copy(), cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        c = max(cnts,key = cv.contourArea)
        
        cv.drawContours(image,[c], -1, (0,255,0),2)
        
        
        cv.putText(image, text, (5,25), cv.FONT_HERSHEY_SIMPLEX, 0.8,color, 2)
        
        # show the output image and edge map
        cv.imshow("Image", image)
        cv.imshow("Edge", edged)
        cv.waitKey(0)