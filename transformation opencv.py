# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 18:22:26 2023

@author: visha
"""

import cv2 as cv
import numpy as np

img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')

## transaltion

def translate(img ,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions =(img.shape[1],img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img,-100,100)
cv.imshow('translated',translated)

##rotate

def rotate(img , angle,rotPoint =None):
    (height , width) = img.shape[:2]
    
    if rotPoint is None:
        rotPoint = (width//2,height//2)
        dimensions =(img.shape[1],img.shape[0])
        
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    
    return cv.warpAffine(img,rotMat,dimensions)

rot = rotate(img,45)
cv.imshow('rotated',rot)


##flipping 

flip = cv.flip(img , 0)
cv.imshow('Flip', flip )
cv.waitKey(0)