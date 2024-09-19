from detection import Detection
from controls import Controls
from window import Window
from time import sleep
from keyboard import is_pressed

win = Window()

def main():
    windows = win.get_windows('Battle | IdleMMO')
    print(windows[0]._hWnd)
    if len(windows) > 0:
        detection = Detection(windows[0]._hWnd)
        controls = Controls(windows[0]._hWnd)
        while not is_pressed('q'):
            battle_button = detection.find_on_screen(
                detection.images['battle'], attempts=5)

            if len(battle_button) > 0:
                print("clicou para atacar")
                controls.mouse_click(battle_button[0])

            start_button = detection.find_on_screen(
                detection.images['start'], attempts=5)

            if len(start_button) > 0:
                print("clicou para caçar")
                controls.mouse_click(start_button[1])

            sleep(10)

if __name__ == '__main__':

    main()
