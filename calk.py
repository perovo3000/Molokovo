import tkinter as tk


def sum():
    s1 = int(ent1.get())
    s2 = int(ent2.get())
    s3 = s1 + s2
    l['text'] = s3
# comment
root = tk.Tk()
ent1 = tk.Entry(width=20)
ent2 = tk.Entry(width=20)
l = tk.Label(width=20)
b = tk.Button(text="Сумма")
b['command'] = sum
ent1.pack()
ent2.pack()
l.pack()
#rjvvtyn
b.pack()
root.mainloop()
