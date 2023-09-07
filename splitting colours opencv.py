# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:39:31 2023

@author: visha
"""

import cv2 as cv
import numpy as np

img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')

blank = np.zeros(img.shape[:2],dtype ='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


cv.imshow('blue', blue)
cv.imshow('green', green)
cv.imshow('red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged =cv.merge([b,g,r])
cv.imshow('merge', merged)

cv.waitKey(0)