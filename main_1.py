"Программа, которая отправляет сообщение, в определенном количествое."

import pyautogui
import  time


print(pyautogui.position()) # Получаем, кординаты курсора.

time.sleep(5)
# pyautogui.moveTo(336, 531, duration=3)

def Roma():
    "Нажимаем на лс Ромы"
    pyautogui.click(x=336, y=531, clicks=1)

def massage():
    pyautogui.write('Privet Roma')

def send_massage():
    'Отправка сообщения'
    pyautogui.press('enter')
    # pyautogui.click(x=1894, y=999, clicks=1)
time.sleep(3)
loop = True
number = 0
# Roma()
while loop:

    pyautogui.write(str(number))
    send_massage()
    number += 1
    if number == 667:          
        loop = False 
 


