import cv2
import numpy as np
import win32gui
import win32ui
from ctypes import windll
from PIL import Image
from PIL import ImageGrab

# get window handle and dimensions 
# Detect the position of The window with Tetris game
windows_list = []
toplist = []
def enum_win(hwnd, result):
    win_text = win32gui.GetWindowText(hwnd)
    windows_list.append((hwnd, win_text))
win32gui.EnumWindows(enum_win, toplist)

 # print(windows_list)

# Game handle
game_hwnd = 0
for (hwnd, win_text) in windows_list:
    if "Photos" in win_text:
        game_hwnd = hwnd

while True:
    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    #left, top, right, bot = win32gui.GetClientRect(game_hwnd)
    left, top, right, bot = win32gui.GetWindowRect(game_hwnd)
    position = win32gui.GetWindowRect(game_hwnd)
    w = right - left
    h = bot - top
    
    hwndDC = win32gui.GetWindowDC(game_hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    
    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    
    saveDC.SelectObject(saveBitMap)
    
    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    result = windll.user32.PrintWindow(game_hwnd, saveDC.GetSafeHdc(), 1)
    #result = windll.user32.PrintWindow(game_hwnd, saveDC.GetSafeHdc(), 0)
    
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    
    im = Image.frombuffer(
            'RGB',
            (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
            bmpstr, 'raw', 'BGRX', 0, 1)
    
    screenshot = ImageGrab.grab(position)
    
    
    
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(game_hwnd, hwndDC)
    
    im = np.array(screenshot)
    im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)
    cv2.imshow("Screen", im)
    key = cv2.waitKey(25)
    if key == 'q':
        break

cv2.destroyAllWindows()