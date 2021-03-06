# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 13:57:20 2020

@author: Steven.Nguyen
"""

import cv2
import numpy as np
from PIL import ImageGrab
import win32gui

# Detect the position of The window with Tetris game
windows_list = []
toplist = []
def enum_win(hwnd, result):
    win_text = win32gui.GetWindowText(hwnd)
    windows_list.append((hwnd, win_text))
win32gui.EnumWindows(enum_win, toplist)

print(windows_list)

# Game handle
game_hwnd = 0
for (hwnd, win_text) in windows_list:
    if "Photos" in win_text:
        game_hwnd = hwnd

while True:
    position = win32gui.GetWindowRect(game_hwnd)


    # Take screenshot
    screenshot = ImageGrab.grab(position)
    screenshot = np.array(screenshot)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)
    cv2.imshow("Screen", screenshot)

    key = cv2.waitKey(25)
    if key == 27:
        break

cv2.destroyAllWindows()