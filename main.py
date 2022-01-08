import webbrowser
import pyautogui
import time

code = input("enter the code: ")

webbrowser.open(f"https://meet.google.com/{code}")

time.sleep(5)

pyautogui.hotkey('ctrl', 'd')
pyautogui.hotkey('ctrl', 'e')
i = 1
while i < 9:
    pyautogui.press('tab')
    i += 1
pyautogui.press('enter')
