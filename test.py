import tkinter as tk
from random import randint

WIDTH = 600
HEIGHT = 400


def tick():
    global ball, canvas, root, x, y, R, dx, dy
    x += dx
    y += dy
    print('x= ', x, "   y= ", y)
    if x - R <= 0 or x + R > WIDTH:
        dx = -dx
    if y - R <= 0 or y + R > HEIGHT:
        dy = -dy
    canvas.move(ball, dx, dy)
    root.after(20, tick)


def main():
    global ball, canvas, root, x, y, R, dx, dy
    dx, dy = [1, 1]
    root = tk.Tk()
    root.title('Boll')
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.pack(anchor='center')
    R = randint(30, 40)
    x = randint(R, WIDTH - R)
    y = randint(R, HEIGHT - R)
    print('R=', R, "  x=", x, "  y=", y)
    ball = canvas.create_oval(x - R, y - R, x + R, y + R, fill='green')
    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
