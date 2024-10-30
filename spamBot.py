import pyautogui
import webbrowser as web
from time import sleep

#web.open("https://web.whatsapp.com/send?phone=+523316043026")
sleep(10)

with open('spam.txt', 'r') as file:
    for line in file:
        pyautogui.typewrite(line)

#for i in range(10):
#    pyautogui.hotkey('command', 'v')
#    pyautogui.press("enter")
