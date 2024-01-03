import smtplib
import ssl
import os


path = os.path.dirname(os.path.abspath(__file__))
script_path_key = os.path.join(path, 'key.txt')


def sendmail():
    smtp_server = "smyp.gmail.com"
    port = 587
    sender_email = "Xendorium@gmail.com"
    password = "Xendorium123"
    receiver_email = "Xendorium@gmail.com"
    contex = ssl.create_default_context()
    msg = "Hello"
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=contex)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg)
    except Exception as e:
        print(e)
    finally:
        server.quit()

