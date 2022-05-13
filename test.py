import tkinter as tk


def tick():
    canvas.move(krug, +10, +10)
    root.after(50, tick)


root = tk.Tk()
root.geometry('600x400')
canvas = tk.Canvas(root)
canvas.pack(anchor='nw')
krug = canvas.create_oval(100, 100, 200, 200, fill='green')
root.mainloop()
