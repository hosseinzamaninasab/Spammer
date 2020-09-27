import pyautogui
import time

time.sleep(8)
text = open('test.txt', 'r')
pyautogui.FAILSAFE = False
for char in text:
    pyautogui.typewrite(char)
    pyautogui.press('enter')
