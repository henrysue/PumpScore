# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 15:45:21 2020

@author: henry.sue
"""

# PumpScores2Final

import cv2
import pytesseract
import numpy as np
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:/Users/hsadmin/AppData/Local/Tesseract-OCR/tesseract.exe' 

img = cv2.imread(r'N:\Temp\Steven Nguyen\pumpscores\data\Raw Data\ragnarok_18_20.png',0)


def thresholding(image):
    return cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)[1]
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

img2 = thresholding(img)



boxlist = [([613, 181, 715, 30],'location'), 
([613, 220, 715, 30],'songname'),
([366, 2, 354, 31],'p1title'),
([366, 33, 160, 29],'p1name'),
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
([300, 270, 198, 45],'plperf'),
([300, 328, 175, 39],'p1great'),
([300, 376, 175, 46],'p1good'),
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
([600, 588, 215, 40],'p1upscore'),
([1082, 588, 220, 40],'p2upscore'),
]

upscores = [
([600, 588, 215, 40],'p1upscore'),
([1082, 588, 220, 40],'p2upscore'),
]

cals = [
([300, 641, 190, 40],'p1cal'),
([1396, 640, 240, 40],'p2cal'),       
]

names = [
([613, 181, 715, 30],'location'), 
([613, 220, 715, 30],'songname'),
([366, 33, 167, 29],'p1name'),
([300, 641, 190, 40],'p1cal'),
([1390, 33, 166, 30],'p2name'),
([1396, 640, 240, 40],'p2cal'),
]

scores = [([300, 589, 245, 40],'p1score'),([1370, 588, 260, 40],'p2score')]

counter = 0
outlist = []

digit_config = r'--oem 3 --psm 6 outputbase digits'
config2 = r'--oem 3 --psm 8'
config1 = r'--oem 3 --psm 6'

numdict = {}
namesdict = {}

for box,tag in numerical:
    roi = img2[box[1]:(box[1]+box[3]),box[0]:(box[0]+box[2])]
    out = pytesseract.image_to_string(roi, lang='Piu', config=digit_config)
    counter += 1
    outlist.append((out,tag))
    numdict.update([(tag,out)])

for box,tag in names:
    roi = img2[box[1]:(box[1]+box[3]),box[0]:(box[0]+box[2])]
    out = pytesseract.image_to_string(roi, lang='Piu+eng',config = config1)
    counter += 1
    outlist.append((out,tag))
    namesdict.update([(tag,out)])


print(namesdict)
print(numdict)
#cv2.imshow("image",img2)
#cv2.waitKey(0)

#cv2.imshow('image',imgcanny)
#cv2.waitKey(0)


#custom_oem_psm_config = r'--oem 3 --psm 4'
#tessdata_dir_config = r'C:\Users\snadmin\AppData\Local\Tesseract-OCR\tesseract.exe "N:\Temp\Steven Nguyen\pumpscores\test.uzn"'
#output = pytesseract.image_to_string(img, config=tessdata_dir_config)


