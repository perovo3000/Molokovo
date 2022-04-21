import tkinter as tk


def button_change():
    butt['text'] = 'Ohh!'


win = tk.Tk()
lab = tk.Label(text='Gjlgbcm',
               font='times.20',
               fg='blue',
               bg='orange',
               height='2',
               width='20')
ent = tk.Entry(font='times.20',
               fg='blue',
               bg='gray')

butt = tk.Button(
    text='Push',
    font='times.20',
    height='2',
    width='10')
butt.config(command=button_change)
lab.pack()
ent.pack()
ent.insert(0, 'ВВедите имя')
name = ent.get()
print(name)
ent.delete(0, tk.END)
butt.pack()
win.mainloop()
