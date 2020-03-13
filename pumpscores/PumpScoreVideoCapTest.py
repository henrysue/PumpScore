# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 16:16:40 2020

@author: Steven.Nguyen
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(1)
cap.set(3,1280)
cap.set(4,720)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imshow('frame',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()