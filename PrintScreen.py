import pyautogui
import os

path = os.path.dirname(os.path.abspath(__file__))
screen_path = os.path.join(path, 'screen.png')


def take_screen():
    screen = pyautogui.screenshot()
    screen.save(screen_path)

