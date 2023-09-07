# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:39:10 2023

@author: visha
"""

import cv2 as cv
import numpy as np

img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')

blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank image',blank)

mask = cv.circle(blank,(img.shape[1]//2 + 150,img.shape[0]//2 - 40),100,255,-1)
cv.imshow('mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)
 

cv.waitKey(0)