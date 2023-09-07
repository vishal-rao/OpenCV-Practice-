# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 14:44:31 2023

@author: visha
"""

import cv2 as cv
import numpy as np 
import imutils 



img = cv.imread('D:/Capstone MSc/example images/hand.jpg')
cv.imshow('hand',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

threshold , thresh = cv.threshold(gray,230,255,cv.THRESH_BINARY_INV)
cv.imshow('Thresh', thresh)


countour = cv.findContours(thresh.copy(), cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
countour = imutils.grab_contours(countour)
c = max(countour , key = cv.contourArea)

##drawing the shape of the contour

out = img.copy()
cv.drawContours(out,[c],-1,(0,255,0),3)

(x,y,w,h) = cv.boundingRect(c)

text = "original, num_pts={}".format(len(c))
cv.putText(out, text, (x, y - 15), cv.FONT_HERSHEY_SIMPLEX,0.9, (0, 255, 0), 2)

##original contour


print("[INFO] {}".format(text))
cv.imshow("Original Contour", out)


# to demonstrate the impact of contour approximation, let's loop
# over a number of epsilon sizes
for eps in np.linspace(0.001, 0.05, 10):
	# approximate the contour
	peri = cv.arcLength(c, True)
	approx = cv.approxPolyDP(c, eps * peri, True)
	# draw the approximated contour on the image
	out = img.copy()
	cv.drawContours(out, [approx], -1, (0, 255, 0), 3)
	text = "eps={:.4f}, num_pts={}".format(eps, len(approx))
	cv.putText(out, text, (x, y - 15), cv.FONT_HERSHEY_SIMPLEX,0.9, (0, 255, 0), 2)
	# show the approximated contour image
	print("[INFO] {}".format(text))
	cv.imshow("Approximated Contour", out)


cv.waitKey(0)
