# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 15:41:44 2020

@author: henry.sue
"""

import numpy as np
import math
import cv2
from matplotlib import pyplot as plt
from scipy import ndimage
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HSadmin\AppData\Local\Tesseract-OCR\tesseract.exe' 

img = cv2.imread(r'C:\Users\henry.sue\Desktop\test.png',0)

# Bounding Boxes

# Format x,y,w,h

location = [613, 181, 715, 30]
songname = [613, 220, 715, 30]

p1name = [366, 33, 167, 29]
p1perf = [300, 270, 198, 45]
p1great = [300, 328, 175, 39]
p1good = [300, 276, 175, 46]
p1bad = [300, 433, 175, 40]
p1miss = [300, 481, 175, 43]
p1combo = [300, 538, 175, 40]
p1score = [300, 589, 245, 40]
p1upscore = [600, 588, 215, 40] 
p1cal = [300, 641, 190, 40]
p1best = [270, 800, 190, 28]
p1machine = [270, 900, 190, 28]
p1machinename = [270, 868, 190, 30]
p2name = [1390, 300, 166, 30]
p2score = [1365, 273, 260, 40]
p2great = [1390, 327, 240, 40]
p2good = [1390, 377, 240, 40]
p2bad = [1390, 432, 240, 40]
p2miss = [1390, 484, 240, 40]
p2combo = [1390, 536, 240 , 40]
p2score = [1370, 588, 270, 40]
p2upscore = [1082, 588, 220, 40]
p2cal = [1396, 640, 240, 40]
p2best = [1460, 796, 191, 30]
p2machine = [1460, 899, 191, 30]
p2machinename = [1460, 867, 190, 30]

