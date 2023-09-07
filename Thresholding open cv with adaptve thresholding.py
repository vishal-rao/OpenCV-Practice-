# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 13:21:25 2023

@author: visha
"""

import cv2 as cv
import numpy as np
import os
img = cv.imread('D:/ML Datasets/MRI/archive/Training/glioma_tumor/gg (2).jpg')
# cv.imshow('cat', img)

##Simple Thresholding 

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

##Simple threshold
threshold , thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('Simple threshold', thresh)

threshold , thresh_inv = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Simple threshold_inverse', thresh_inv)



## adaptive thresholding 

adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV ,15,9)
cv.imshow('adaptive threshold', adaptive_thresh)

cv.waitKey(0)