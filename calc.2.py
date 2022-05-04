import tkinter as tk

dat = []


def get_data():
    dat = []
    d = int(ent1.get())
    dat.append(d)
    d2 = int(ent2.get())
    dat.append(d2)
    return dat


def plus():
    k = get_data()
    sum = k[0] + k[1]
    lbl1['text'] = sum


def minus():
    pass


def mult():
    pass


def div():
    pass


root = tk.Tk()
lbl = tk.Label(text='Calkulator')
lbl1 = tk.Label(font='Arial 16')
ent1 = tk.Entry()
ent2 = tk.Entry()
btn1 = tk.Button(text='+', font='Arial 15')
btn2 = tk.Button(text='-', font='Arial 15')
btn3 = tk.Button(text='*', font='Arial 15')
btn4 = tk.Button(text='/', font='Arial 15')
btn1['command'] = plus
btn2['command'] = minus
btn3['command'] = mult
btn4['command'] = div
# lbl.pack()
# lbl1.pack()
ent1.grid(row=0, column=0, ipadx=100, ipady=10, padx=5, pady=5)
ent2.grid(row=0, column=1, ipadx=100, ipady=10)
btn1.grid(row=1, column=0, ipadx=100, ipady=1, padx=5, pady=5)
btn2.grid(row=1, column=1, ipadx=100, ipady=1, padx=5, pady=5)
btn3.grid(row=2, column=0, ipadx=100, ipady=1, padx=5, pady=5)
btn4.grid(row=2, column=1, ipadx=100, ipady=1, padx=5, pady=5)
lbl1.grid(row=3)
# lbl1.gird(row=3, column=0)
root.mainloop()
