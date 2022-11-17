import os
import time
import tkinter as tk

def button_1():
    name1 = ent1.get()
    print(name1)
    name2 = ent2.get()
    print(name2)

roof = tk.Tk()
lab = tk.Label(text='Ахиватор tar( Wimdows 10)',
               font='times.20',
               fg='blue',
               height='1',
               width='50')
lab1 = tk.Label(text='Введите путь архивируемого файла и его имя С:\  \имя файла.* ',
               font='times.10',
               fg='blue',
               height='1',
               width='60')
ent1 = tk.Entry(font='times.10',
               fg='blue',
               bg='gray',
               width ='60')
butt_1 = tk.Button(
    text='ВВод',
    fg='blue',
    font='times.10',
    height='1',
    width='10')
butt_1.config(command=button_1)
lab2 = tk.Label(text='Введите путь куда архивировать  файл и его имя С:\  \имя файла.* ',
               font='times.10',
               fg='blue',
               height='1',
               width='60')
ent2 = tk.Entry(font='times.10',
               fg='blue',
               bg='gray',
               width='60')
lab.pack()
lab1.pack()
ent1.pack()

lab2.pack()
ent2.pack()
butt_1.pack()
roof.mainloop()


