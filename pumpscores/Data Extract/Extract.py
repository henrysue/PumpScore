# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 08:59:49 2020

@author: henry.sue
"""

import cv2
import pytesseract
import numpy as np
from pytesseract import Output
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/hsadmin/AppData/Local/Tesseract-OCR/tesseract.exe' 

img = cv2.imread(r'N:\Temp\Steven Nguyen\pumpscores\test.png',0)

def thresholding(image):
    return cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]

boxlist = [([613, 181, 715, 30],'location'), 
([613, 220, 715, 30],'songname'),
([366, 2, 354, 31],'p1title'),
([366, 33, 167, 29],'p1name'),
([13, 253, 68, 58],'p1speed'),
([300, 270, 198, 45],'p1perf'),
([300, 328, 175, 39],'p1great'),
([300, 376, 175, 46],'p1good'),
([300, 433, 175, 40],'p1bad'),
([300, 481, 175, 43],'p1miss'),
([300, 538, 175, 40],'p1combo'),
([300, 589, 245, 40],'p1score'),
([600, 588, 215, 40],'p1upscore'),
([300, 641, 190, 40],'p1cal'),
([270, 800, 190, 28],'p1best'),
([270, 900, 190, 28],'p1machine'),
([270, 868, 190, 30],'p1machinename'),
([445, 366, 409, 212],'p1grade'),
([599, 727, 227, 227],'p1level'),
([1199, 2, 356, 31],'p2title'),
([1390, 33, 166, 30],'p2name'),
([1837, 255, 70, 55],'p2speed'),
([1365, 273, 260, 40],'p2perf'),
([1390, 327, 240, 40],'p2great'),
([1390, 377, 240, 40],'p2good'),
([1390, 432, 240, 40],'p2bad'),
([1390, 484, 240, 40],'p2miss'), 
([1390, 536, 240 , 40],'p2combo'),
([1370, 588, 260, 40],'p2score'),
([1082, 588, 220, 40],'p2upscore'),
([1396, 640, 240, 40],'p2cal'),
([1460, 796, 191, 30],'p2best'),
([1460, 899, 191, 30],'p2machine'),
([1460, 867, 190, 30],'p2machinename'),
([1098, 369, 409, 210],'p2grade'),
([1091, 727, 227, 227],'p2level')]

numerical = [
([300, 270, 198, 45],'p1perf'),
([300, 328, 175, 39],'p1great'),
([300, 328, 175, 39],'p1great'),
([300, 433, 175, 40],'p1bad'),
([300, 481, 175, 43],'p1miss'),
([300, 538, 175, 40],'p1combo'),
([300, 589, 245, 40],'p1score'),
([1365, 273, 260, 40],'p2perf'),
([1390, 327, 240, 40],'p2great'),
([1390, 377, 240, 40],'p2good'),
([1390, 432, 240, 40],'p2bad'),
([1390, 484, 240, 40],'p2miss'), 
([1390, 536, 240 , 40],'p2combo'),
([1370, 588, 260, 40],'p2score'),
        ]

upscores = [
([600, 588, 215, 40],'p1upscore'),
([1082, 588, 220, 40],'p2upscore'),
        ]

cals = [
([300, 641, 190, 40],'p1cal'),
([1396, 640, 240, 40],'p2cal'),       
        ]

counter = 0
for filename in os.listdir(r'N:\Temp\Steven Nguyen\pumpscores\data\Titled\\'):
    if filename.endswith('.tif'):
        img = cv2.imread(r'N:\Temp\Steven Nguyen\pumpscores\data\Titled\\'+filename,0)
        for row in numerical:
            imgloc = img[row[0][1]:(row[0][1]+row[0][3]),row[0][0]:(row[0][0]+row[0][2])]
            imgloc2 = thresholding(imgloc)
            img2 = Image.fromarray(imgloc2)
            img2.save('N:\Temp\Steven Nguyen\pumpscores\data\Extract\\'+str(counter)+'.tif')
            counter+=1
        continue
    else:
        continue
  