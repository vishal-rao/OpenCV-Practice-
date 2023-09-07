# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 14:11:44 2023

@author: visha
"""

import cv2 as cv
import numpy as np
img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')
cv.imshow('cat', img)

##laplacian 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplacian',lap)


##sobel 
sobelx = cv.Sobel(gray,cv.CV_64F,1, 0)
sobely = cv.Sobel(gray,cv.CV_64F,0, 1)
combined_model = cv.bitwise_or(sobelx, sobely)

#canny 

canny = cv.Canny(gray,150,175)
cv.imshow('canny ', canny )


cv.imshow('sobel X', sobelx)
cv.imshow('sobel y', sobely)
cv.imshow('combined', combined_model)
cv.waitKey(0)