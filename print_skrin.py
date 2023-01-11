import pyautogui
import webbrowser
import time

# задаем количество страниц, клторых необходимо отпринскринить
namber_screen = int(input("Вести число страниц   "))
for i in range(1, namber_screen + 1):
    screen = 'scr_' + str(i) + '.png'
    # вводим адрес страницы для принтскрина i - меняющийся номер HTML страницы
    http = 'https://sdo.itsecurity.ru/UCV3/KP06_v7_h5LLwee/' + str(i + 1) + '/index.html#zoom=z'
    # открываем необходимую страницу в браузере по умолчанию
    webbrowser.open(http, new=0)
    # необходимо время задержки, для отурытия страницы в браузере
    time.sleep(3)
    # делаем непосредственно printscreen
    pyautogui.screenshot(screen)

# !!!! ALT - Tab для переключение между браузером и запуска Scrept
