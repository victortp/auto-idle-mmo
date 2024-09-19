import cv2 as cv
import numpy as np
from os import listdir
from os.path import isfile, join
from time import sleep
from pathlib import Path
import win32gui, win32ui
from PIL import Image
import ctypes

class Detection:
    images = {}
    number_images = {}
    _hWnd = 0

    def __init__(self, hWnd = 0):
        self.images = self.load_images()
        self._hWnd = hWnd

    def load_images(self, dirname=Path('img/')):
        files = [f for f in listdir(
            dirname) if isfile(join(dirname, f))]

        img = {}

        for file in files:
            img[file[:-4]] = cv.imread(join(dirname, file))

        return img

    def get_screenshot(self):
        w = 1920
        h = 1080
        hwndDC = win32gui.GetWindowDC(self._hWnd)
        mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
        saveDC = mfcDC.CreateCompatibleDC()

        saveBitMap = win32ui.CreateBitmap()
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
        saveDC.SelectObject(saveBitMap)    
        ctypes.windll.user32.PrintWindow(self._hWnd, saveDC.GetSafeHdc(), 2)
        bmpstr = saveBitMap.GetBitmapBits(True)
        
        win32gui.DeleteObject(saveBitMap.GetHandle())
        saveDC.DeleteDC()
        mfcDC.DeleteDC()
        win32gui.ReleaseDC(self._hWnd, hwndDC)

        img = Image.frombuffer('RGB', (w, h), bmpstr, 'raw', 'BGRX', 0, 1)
        img.save('teste.png')
        img = np.array(img)
        img = img[:, :, ::-1].copy()

        return img

    def find_on_screen(self, target, screenshot=None, threshold=0.7, attempts=1):
        if screenshot is None:
            screenshot = self.get_screenshot()

        result = cv.matchTemplate(
            screenshot, target, cv.TM_CCOEFF_NORMED)

        h, w, _ = target.shape

        locations = np.where(result >= threshold)
        rectangles = []
        for (x, y) in zip(*locations[::-1]):
            rectangles.append((x, y, w, h))

        if len(rectangles) > 0 or attempts == 1:
            return rectangles

        sleep(1)

        return self.find_on_screen(target, None, threshold, attempts=attempts-1)
