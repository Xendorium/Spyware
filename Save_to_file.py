import os

path = os.path.dirname(os.path.abspath(__file__))
script_path = os.path.join(path, 'key.txt')


def save_to_file(data):
    file = open(script_path, 'a')
    file.write(data)
    file.close()


