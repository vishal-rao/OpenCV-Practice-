# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 18:58:34 2023

@author: visha
"""

import cv2 as cv
import numpy as np

img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')


blank = np.zeros(img.shape,dtype ='uint8')
blur = cv.GaussianBlur(img,(5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur',blur)

gray = cv.cvtColor(blur,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

canny = cv.Canny(img,125,175)
cv.imshow('canny edges', canny)

# ret ,thresh =cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('thres',thresh)

contours, hierachies = cv.findContours(canny,cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found')

cv.drawContours(blank,contours,-1,(0,0,255),2)

cv.imshow('count',blank)


cv.waitKey(0)