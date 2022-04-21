class Car():

    def __init__(self, mark, year):
        self.mark = mark
        self.year = year
        self.odometr = 10

    def show(self):
        print('My car is  \n' + self.mark.title())
        print('Year - \n' + str(self.year))
        self.odometr += 10
        print('New odometr\n' + str(self.odometr))

n = int(input('Namber of cars  '))
for i in range(n):
    m = input('Марка авто  ')
    y = int(input("Год выпуска  "))
    my_car1 = Car(m, y)
    my_car1.show()
