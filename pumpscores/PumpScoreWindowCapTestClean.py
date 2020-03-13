# imports
import cv2
import numpy as np
import win32gui, win32con, ctypes  
from PIL import ImageGrab

class ExtractImageWidget(object):
    def __init__(self):
        self.original_image = cv2.imread(r'N:\Temp\Steven Nguyen\pumpscores\test.png',)
        self.clone = self.original_image.copy()

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.extract_coordinates)

        # Bounding box reference points and boolean if we are extracting coordinates
        self.image_coordinates = []
        self.extract = False

    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x,y)]
            global coords 
            coords = [(x,y)]
            self.extract = True

        # Record ending (x,y) coordintes on left mouse bottom release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x,y))
            coords.append((x,y))
            self.extract = False
            print('top left: {}, bottom right: {}'.format(self.image_coordinates[0], self.image_coordinates[1]))
            print('x,y,w,h : ({}, {}, {}, {})'.format(self.image_coordinates[0][0], self.image_coordinates[0][1], self.image_coordinates[1][0] - self.image_coordinates[0][0], self.image_coordinates[1][1] - self.image_coordinates[0][1]))
            

            # Draw rectangle around ROI
            cv2.rectangle(self.clone, self.image_coordinates[0], self.image_coordinates[1], (0,255,0), 2)
            cv2.imshow("image", self.clone) 

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.original_image.copy()

    def show_image(self):
        return self.clone

dimensions = (coords[0][0], rect.top, rect.right, rect.bottom)        


# this takes care of the DPI settings (https://stackoverflow.com/questions/51786794/using-imagegrab-with-bbox-from-pywin32s-getwindowrect)
ctypes.windll.user32.SetProcessDPIAware()

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

image = ImageGrab.grab(win32gui.GetWindowRect(game_hwnd))
extract_image_widget = ExtractImageWidget(image)
while True:
    cv2.imshow('image', extract_image_widget.show_image())
    key = cv2.waitKey(0)

# Close program with keyboard 'q'
    if key == ord('q'):
        cv2.destroyAllWindows()
        exit()


while True:
    dimensions = win32gui.GetWindowRect(game_hwnd)    

    # this gets the window size, comparing it to `dimensions` will show a difference
    winsize = win32gui.GetClientRect(game_hwnd)

    # this sets window to front if it is not already
    win32gui.SetWindowPos(game_hwnd, win32con.HWND_NOTOPMOST,0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    win32gui.SetWindowPos(game_hwnd, win32con.HWND_TOPMOST,0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    win32gui.SetWindowPos(game_hwnd, win32con.HWND_NOTOPMOST,0,0,0,0, win32con.SWP_SHOWWINDOW | win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

    # grab screen region set in `dimensions`
    image = ImageGrab.grab(dimensions)

    # we're going to use this to get window attributes
    f=ctypes.windll.dwmapi.DwmGetWindowAttribute

    # `rect` is for the window coordinates
    rect = ctypes.wintypes.RECT()
    DWMWA_EXTENDED_FRAME_BOUNDS = 9

    # and then the coordinates of the window go into `rect`
    f(ctypes.wintypes.HWND(game_hwnd),
      ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
      ctypes.byref(rect),
      ctypes.sizeof(rect)
      )

    # if we want to work out the window size, for comparison this should be the same as `winsize`
    size = (rect.right - rect.left, rect.bottom - rect.top)        

    # put the window coordinates in a tuple like that returned earlier by GetWindowRect()
    dimensions = (rect.left, rect.top, rect.right, rect.bottom)

    # grab screen region set in the revised `dimensions`
    image = ImageGrab.grab(dimensions)
    image = np.array(image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    
    cv2.imshow("Screen", image)
    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()