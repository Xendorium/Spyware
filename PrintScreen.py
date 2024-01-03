import pyautogui
import os
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__))


def take_screen():
    time = datetime.now()
    hour = str(time.hour)
    minute = str(time.minute)
    screen_path = os.path.join(path, f'screen-{hour}-{minute}.png')
    screen = pyautogui.screenshot()
    screen.save(screen_path)


