import tkinter as tk

def get_data():
    s=[]
    s1 = int(ent1.get())
    s.append(s1)
    s2 = int(ent2.get())
    s.append(s2)
    return s

def sum1():
    k=get_data()
    rezultat=k[0]+k[1]
    lab1['text'] = rezultat


def umn():
    k = get_data()
    rezultat = k[0] * k[1]
    lab1['text'] = rezultat


def del1():
    k = get_data()
    rezultat = k[0] /k[1]
    lab1['text'] = rezultat


def minus():
    k = get_data()
    rezultat = k[0] / k[1]
    lab1['text'] = rezultat

root = tk.Tk()
lab = tk.Label(text='Caculator')
lab1=tk.Label(width=20)
ent1 = tk.Entry(width=20)
ent2 = tk.Entry(width=20)
b1 = tk.Button(text="+")
b2 = tk.Button(text="-")
b3 = tk.Button(text='/')
b4 = tk.Button(text='*')
b1['command'] = sum1
b2['command'] = minus
b3['command'] = del1
b4['command'] = umn
lab.pack()
lab1.pack()
ent1.pack()
ent2.pack()
b1.pack()
b2.pack()
b3.pack()
b4.pack()
root.mainloop()
