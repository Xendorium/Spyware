import pyautogui
import os


path = os.path.dirname(os.path.abspath(__file__))



def take_screen(number):
    screen_path = os.path.join(path, f'screen{number}.png')
    screen = pyautogui.screenshot()
    screen.save(screen_path)



