# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:50:41 2023

@author: visha
"""

import cv2 as cv
import numpy as np

img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')

##Averaging 
average = cv.blur(img,(3,3))
cv.imshow('average',average)

## gaussian blur
gaus = cv.GaussianBlur(img, (3,3),0)
cv.imshow('gaus',gaus)

##medianblur

med = cv.medianBlur(img,3)
cv.imshow('median',med)

##bilateral
bilat = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral',bilat)

cv.waitKey(0)