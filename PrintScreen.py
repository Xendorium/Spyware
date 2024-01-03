import pyautogui
import os
import datetime

path = os.path.dirname(os.path.abspath(__file__))



def take_screen(number):
    time = datetime.now()
    screen_path = os.path.join(path, f'screen{time}.png')
    screen = pyautogui.screenshot()
    screen.save(screen_path)



