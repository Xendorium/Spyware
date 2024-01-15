import pyautogui
import os
import shutil
from datetime import datetime

path = os.path.dirname(os.path.abspath(__file__))
dir = "screens"


def take_screen():

    time = datetime.now()
    hour = str(time.hour)
    minute = str(time.minute)
    if not os.path.exists(os.path.join(path, dir)):
        os.makedirs(os.path.join(path, dir))
    screen_path = os.path.join(path, dir, f'screen-{hour}-{minute}.png')
    screen = pyautogui.screenshot()
    screen.save(screen_path)


def clear():
    screen_path = os.path.join(path, dir)
    items = os.listdir(screen_path)
    shutil.rmtree(screen_path)
    os.makedirs(screen_path, exist_ok=True)
    if os.path.exists(screen_path):
        os.rmdir(screen_path)

