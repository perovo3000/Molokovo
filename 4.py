import tkinter as tk


def change_button():
    butt['text'] = 'CHANGE'
    butt['bg'] = '#000000'
    butt['fg'] = '#ffffff'
    butt['background'] = '#555555'


window = tk.Tk()
butt = tk.Button(text='Нажми меня',
                 font='Arial 20',
                 height=2,
                 width=10
                 )
butt.config(command=change_button)
butt.pack()
window.mainloop()
