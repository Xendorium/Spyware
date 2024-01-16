from cryptography.fernet import Fernet
import os

path = os.path.dirname(os.path.abspath(__file__))
script_path_encryptkey = os.path.join(path, 'encryptkey.txt')


def generate_key():
    key = Fernet.generate_key()
    with open(script_path_encryptkey, 'wb') as file:
        file.write(key)
    return key


def crypt_file(file):
    key = generate_key()
    fernet = Fernet(key)
    with open(file, 'rb') as file_2:
        orginal = file_2.read()
    encrypted_file = fernet.encrypt(orginal)
    with open(file, 'wb') as e_file:
        e_file.write(encrypted_file)


def clear():
    if os.path.exists(script_path_encryptkey):
        os.remove(script_path_encryptkey)