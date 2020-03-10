# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 10:23:36 2020

@author: henry.sue
"""

# Padding all extracted images for training

import os
from PIL import Image
import cv2
import numpy as np

counter = 0
for filename in os.listdir('N:\Temp\Steven Nguyen\pumpscores\data\Extract'):
        if filename.endswith('.tif'):
            img = cv2.imread(r'N:\Temp\Steven Nguyen\pumpscores\data\Extract\\'+filename,0)
            img2 = np.invert(img)
            imgload = Image.fromarray(img2)
            imgload.save(r'N:\Temp\Steven Nguyen\pumpscores\data\Inverted\\'+str(counter)+'.tif')
            counter += 1
            continue
        else:
            continue
            
        