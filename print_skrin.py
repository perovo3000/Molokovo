import pyautogui
import webbrowser

webbrowser.open('https: // sdo.itsecurity.ru / UCV3 / BT01_v7Thj / index.html', new = 2)
namber_screen = int(input("Вести число страниц   "))
for i in range(1, namber_screen + 1):
    screen = 'scr_' + str(i) + '.png'
    pyautogui.screenshot(screen, region=(100, 100, 1800, 1000))
