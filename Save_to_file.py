import os

path = os.path.dirname(os.path.abspath(__file__))
script_path_key = os.path.join(path, 'key.txt')
script_path_emails = os.path.join(path, 'emails.txt')


def save_to_file(data):
    file = open(script_path_key, 'a')
    file.write(data)
    file.close()


def clear_key():
    if os.path.exists(script_path_key):
        os.remove(script_path_key)

