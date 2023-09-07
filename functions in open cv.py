# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 16:22:39 2023

@author: visha
"""

import cv2 as cv

img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')

# def rescaleFrame(frame , scale = 0.25):
#     width = int(frame.shape[1] * scale)
#     height = int(frame.shape[0] * scale)
#     dimensions = (width, height)
    
#     return cv.resize(frame, dimensions , interpolation=cv.INTER_AREA)

## grey
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)



##Blur
blur= cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('cat',blur)

##edge cascade

canny = cv.Canny(blur,125,175)
cv.imshow('cat0',canny)


##dilatig image
dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('cat1',dilated)


##erodingf 

erd = cv.erode(dilated, (3,3),iterations= 1)
cv.imshow('cat2', erd)

##reszie

rez = cv.resize(img, (500,500),interpolation = cv.INTER_CUBIC)
cv.imshow('rez', rez)
cv.waitKey(0)
# capture = cv.VideoCapture(0)

# while True:
#     isTrue , frame = capture.read()
#     cv.imshow('video',frame)
    
#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break
# capture.release()
# cv.destroyAllWindows()