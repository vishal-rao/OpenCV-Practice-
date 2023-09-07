# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:28:17 2023

@author: visha
"""

import cv2 as cv
import numpy as np

img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

##bitwise and
bitwise = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise and', bitwise)

##bitwise or
bitor = cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise or', bitor)

##bitwise Xor

bitxor = cv.bitwise_xor(rectangle,circle)
cv.imshow('bitwise xor', bitxor)

##bitwise not 

bitnot  = cv.bitwise_not(bitxor)
cv.imshow('not ',bitnot )

cv.waitKey(0)