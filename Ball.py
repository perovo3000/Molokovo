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
    global root, canvas, ball
    global ball_id, x, y, z, r
    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.place(width=600, height=400)
    r = randint(20, 50)
    x = randint(r, WIDTH - r)
    y = randint(r, HEIGHT - r)
    ball = canvas.create_oval(x - r, y - r, x + r, y + r, fill='green')
    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
