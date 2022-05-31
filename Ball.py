import tkinter as tk
from random import randint

HEIGHT = 400
WIDTH = 600


def tick():
    global x, y, r, ball, canvas
    dx = 1
    dy = 1
    x += dx
    y += dy
    if x - r <= 0 or x + r > WIDTH:
        dx = -dx
    if y - r <= 0 or y + r > HEIGHT:
        dy = -dy
    canvas.move(ball, dx, dy)
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
