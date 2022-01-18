"х=861  y=455"
"х=880  y=524"
'+- 69 пикселей'

import pyautogui
import time

time.sleep(7)

loop = True
number = 0
i = -900
while loop:
    "На 90 пикселей вниз"
    pyautogui.move(0, 90, duration=0.5)
    pyautogui.click(clicks=1)

    "Нажать на кнопку 'Отправить сообщение'"
    pyautogui.moveTo(x=847, y=536, duration=0.5)
    pyautogui.click()

    pyautogui.moveTo(x=890, y=608, duration=0.5)
    pyautogui.click()

    "Выход из ЛС"
    pyautogui.moveTo(x=758, y=60, duration=0.5)
    pyautogui.click()

    "Нажать на канал"
    pyautogui.click(x=1027, y=48)


    pyautogui.move(0, 100, duration=0.5)

    pyautogui.scroll(i)
    i -= 90
    number += 1
    
    if number == 1:
        loop = False





