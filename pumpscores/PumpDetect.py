# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 16:01:12 2020

@author: henry.sue
"""
import numpy as np
import math
import cv2
from matplotlib import pyplot as plt
from scipy import ndimage
import pytesseract

boxeslist = []

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\hsadmin\AppData\Local\Tesseract-OCR\tesseract.exe' 
img = cv2.imread(r'N:\Temp\Steven Nguyen\pumpscores\test.png')

boxlist = [[613, 181, 715, 30], 
[613, 220, 715, 30],
[366, 2, 354, 31],
[366, 33, 167, 29],
[13, 253, 68, 58],
[300, 270, 198, 45],
[300, 328, 175, 39],
[300, 376, 175, 46],
[300, 433, 175, 40],
[300, 481, 175, 43],
[300, 538, 175, 40],
[300, 589, 245, 40],
[600, 588, 215, 40],
[300, 641, 190, 40],
[270, 800, 190, 28],
[270, 900, 190, 28],
[270, 868, 190, 30],
[445, 366, 409, 212],
[599, 727, 227, 227],
[1199, 2, 356, 31],
[1390, 33, 166, 30],
[1837, 255, 70, 55],
[1365, 273, 260, 40],
[1390, 327, 240, 40],
[1390, 377, 240, 40],
[1390, 432, 240, 40],
[1390, 484, 240, 40], 
[1390, 536, 240 , 40],
[1370, 588, 260, 40],[1082, 588, 220, 40],
[1396, 640, 240, 40],[1460, 796, 191, 30],
[1460, 899, 191, 30],[1460, 867, 190, 30],
[1098, 369, 409, 210],[1091, 727, 227, 227]]

recs = img.copy()
for line in boxlist:
    recs = cv2.rectangle(recs, (line[0],line[1]), ((line[0]+line[2]),(line[1]+line[3])), (0,255,0),2)

cv2.imshow("image",recs)
cv2.waitKey(0)


#plt.imshow(img, cmap='gray')
#plt.xticks([]), plt.yticks([])
#plt.show()

