import cv2
import pytesseract
import numpy as np
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\snadmin\AppData\Local\Tesseract-OCR\tesseract.exe' 

img = cv2.imread(r'N:\Temp\Steven Nguyen\pumpscores\test.png',0)

def thresholding(image):
    return cv2.threshold(image, 0,255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

imgthresh = thresholding(img)

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

textlist = []
counter = 0
tessdata_dir_config = r' --tessdata-dir "C:\Users\snadmin\AppData\Local\Tesseract-OCR\tessdata" --psm 4'

for box in boxlist:
    roi = imgthresh[box[1]:(box[1]+box[3]),box[0]:(box[0]+box[2])]
    out = pytesseract.image_to_string(roi)
    counter +=1
    textlist.append(out)

#tessdata_dir_config = r' --tessdata-dir "C:\Users\snadmin\AppData\Local\Tesseract-OCR\tessdata" --psm 4'
#output = pytesseract.image_to_string(img, config=tessdata_dir_config)

print(textlist)