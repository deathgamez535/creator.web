import random
import time
import pyautogui

while True:

   Y = random.randint(100, 500)
   x = random.randint(100, 500)
   pyautogui.moveTo(x, Y, duration=0.1)
   time.sleep(2)



