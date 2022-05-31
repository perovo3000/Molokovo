import tkinter as tk
from random import randint

WIDTH = 600
HEIGHT = 400


class Ball():
    def __init__(self):
        self.R = randint(30, 40)
        self.x = randint(self.R, WIDTH - self.R)
        self.y = randint(self.R, HEIGHT - self.R)
        self.dx, self.dy = [1, 1]
        self.ball_create = canvas.create_oval(self.x - self.R,
                                              self.y - self.R,
                                              self.x + self.R,
                                              self.y + self.R,
                                              fill='green')

    def move_ball(self):

        self.x += self.dx
        self.y += self.dy
        # опрееление направления шага по осям
        if self.x - self.R <= 0 or self.x + self.R > WIDTH:
            self.dx = -self.dx
        if self.y - self.R <= 0 or self.y + self.R > HEIGHT:
            self.dy = -self.dy

    def show_ball(self):
        canvas.move(self.ball_create, self.dx, self.dy)
        # добавление шага dx.dy, к начальной(внутренней) координате


def tick():
    for ball in balls:
        ball.move_ball()
        ball.show_ball()
    root.after(20, tick)


def main():
    global canvas, root, balls
    global canvas, root, ball

    root = tk.Tk()
    root.title('Ball')
    root.geometry(str(WIDTH) + "x" + str(HEIGHT))
    canvas = tk.Canvas(root)
    canvas.place(width=600, height=400)
    balls = [Ball() for i in range(4)]
    tick()
    root.mainloop()


if __name__ == "__main__":
    main()
