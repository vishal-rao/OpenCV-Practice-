# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:23:50 2023

@author: visha
"""

import cv2 as cv
import numpy as np
import matplotlib.pyplot as ply

img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')


gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)


## BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV',hsv)

##l*a*b

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB',lab)

##BGR TO RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('bgrtorgb',rgb)

##hsv to bgr
bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('bgr',bgr)


cv.waitKey(0)