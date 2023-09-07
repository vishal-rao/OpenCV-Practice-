# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:27:54 2023

@author: visha
"""

import cv2 as cv 
import numpy as np 
from imutils import paths
import imutils
import os 

file_path  = r'D:\ML Datasets\Apples2Oranges.v1i.folder\train\stitch'
image = []
for i in os.listdir(file_path):
    img = os.path.join(file_path, i)
    img2 = cv.imread(img)
    image.append(img2)
    
##sticthing 

print('Stitching images')

stitcher = cv.Stitcher_create(False) if imutils.is_cv3() else cv.Stitcher_create()
(status, stitched) = stitcher.stitch((image))

# if the status is '0', then OpenCV successfully performed image
# stitching
if status == 0:
	# write the output stitched image to disk
	
	# display the output stitched image to our screen
	cv.imshow("Stitched", stitched)
	cv.waitKey(0)
# otherwise the stitching failed, likely due to not enough keypoints)
# being detected
else:
	print("[INFO] image stitching failed ({})".format(status))

cv.waitKey(0)