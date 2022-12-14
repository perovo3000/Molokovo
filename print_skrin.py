import pyautogui
import webbrowser
import time

# задаем количество страниц, клторых необходимо отпринскринить
namber_screen = int(input("Вести число страниц   "))
for i in range(1, namber_screen + 1):
    screen = 'scr_' + str(i) + '.png'
# вводим адрес страницы для принтскрина i - меняющийся номер HTML страницы
    http = 'https://sdo.itsecurity.ru/UCV3/BT01_v7Thj/'+str(i+1)+'/index.html'
# открываем необходимую страницу в браузере по умолчанию
    webbrowser.open(http, new=0)
# необходимо время задержки, для отурытия страницы в браузере
    time.sleep(5)
# делаем непосредственно printscreen
    pyautogui.screenshot(screen, region=(100, 100, 1800, 1000))

#!!!! ALT - Tab для переключение между браузером и запуска Scrept
