import tkinter as tk
from random import randint

HEIGHT = 400
WIDTH = 600

root = tk.Tk()
root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
canvas = tk.Canvas(root)
canvas.place(width=600, height=400)
r = randint(20, 50)
x = randint(r, WIDTH - r)
y = randint(r, HEIGHT - r)
canvas.create_oval(x - r, y - r, x + r, x + r, fill='green')
print(x+r-x-r)
root.mainloop()