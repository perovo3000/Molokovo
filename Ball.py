import tkinter as tk
from random import randint

HEIGHT = 400
WIDTH = 600


def tick():
    ball()
    # x += 1
    # y += 1
    # canvas.move(ball)
    root.after(50, tick)


def main():
    global root, canvas
    global ball_id, x, y, z
    root = tk.Tk()
    root.geometry(str("HEIGHT") + 'x' + str('WIDTH'))
    canvas = tk.Canvas(root)
    canvas.pack(anchor='nw', fill=tk.BOTH)

    r = randint(20, 50)
    x = randint(r, WIDTH - r)
    y = randint(r, HEIGHT - r)
    ball = canvas.create_oval(x - r, y - r, x + r, x + r, fill='green')
    tick()
    root.mainloop()


if __name__ == '__main':
    main()
