import pyautogui
import time
import keyboard

battle_img = '.\\img\\battle.png'
start_img = '.\\img\\start.png'

last_refresh = time.time()
while not keyboard.is_pressed('q'):
    time.sleep(3)
    now = time.time() 
    if now - last_refresh >= 600:
        print('Recarregando a página')
        pyautogui.hotkey('ctrl', 'f5')
        last_refresh = now
        time.sleep(10)

    try:
        battle_location = pyautogui.locateCenterOnScreen(battle_img, grayscale=False, confidence=0.95)
        if battle_location:
            pyautogui.click(battle_location)
            time.sleep(10)
            continue    
    except:
        print('Não encontrou battle')
    
    try:
        start_location = pyautogui.locateCenterOnScreen(start_img, grayscale=False, confidence=0.95)
        if start_location:
            pyautogui.click(start_location)
    except:
        print('Não encontrou start')
