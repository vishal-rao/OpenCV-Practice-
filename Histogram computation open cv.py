# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 12:53:11 2023

@author: visha
"""

import cv2 as cv
import numpy as np

import matplotlib.pyplot as plt

img = cv.imread('D:/Capstone MSc/example images/HD-wallpaper-cat-red-cat-ginger-cats.jpg')

blank = np.zeros(img.shape[:2],dtype='uint8')
# cv.imshow('blank image',blank)


# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)


circle = cv.circle(blank,(img.shape[1]//2 + 150,img.shape[0]//2 - 40), 100, 255,-1)
# cv.imshow('circle',circle)

mask = cv.bitwise_and(img , img , mask = circle)
cv.imshow('mask',mask)
 
##grayscale histogram

# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

mask = cv.circle(blank,(img.shape[1]//2 + 150,img.shape[0]//2 - 40), 100, 255,-1)
# cv.imshow('circle',circle)

masked = cv.bitwise_and(img , img , mask = mask)
cv.imshow('mask',masked)
 


plt.figure()
plt.title('color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b','g','r')
for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask , [256],[0,256])
    plt.plot(hist,color = col)
    plt.xlim([0,256])
plt.show()


cv.waitKey(0)