import win32api, win32gui, win32con

class Controls:
    _hWnd = 0

    def __init__(self, hWnd = 0):
        self.hWnd = hWnd

    def mouse_click(self, rectangle):
        click_pos = self.get_click_position(rectangle)
        click = win32api.MAKELONG(click_pos[0], click_pos[1])
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, click)
        win32gui.SendMessage(self.hWnd, win32con.WM_LBUTTONUP, None, click)

    def get_click_position(self, rectangle):
        x, y, w, h = rectangle

        return ((int(x-8+w/2), int(y-8+h/2)))

