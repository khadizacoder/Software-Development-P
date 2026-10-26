import pyautogui
import time

n = int(input())

time.sleep(5)

for i in range(1, n+1):
    ster = '#' * i

    pyautogui.write(ster)
    pyautogui.press("enter")


