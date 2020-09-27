import pyautogui
import time

time.sleep(5)
pyautogui.FAILSAFE = False
message = 'Bye World'
while True:
    pyautogui.typewrite(message)
    pyautogui.press('enter')
