import os
import re

path = os.path.dirname(os.path.abspath(__file__))
script_path_key = os.path.join(path, 'key.txt')
script_path_emails = os.path.join(path, 'emails.txt')


def save_to_file(data):
    file = open(script_path_key, 'a')
    file.write(data)
    file.close()


def looking_for_emails():
    patern_one = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    patern_two = re.compile(r'(?=^.{6,}$)(?=.*\d)(?=.*[a-zA-Z])')
    file = open(script_path_key, 'r')
    text = file.read()
    match = patern_one.search(text)
    if match:
        file_2 = open(script_path_emails, 'a')
        file_2.write(str(match))
        file.close()
        file_2.close()


def clear_key():
    if os.path.exists(script_path_key):
        os.remove(script_path_key)


