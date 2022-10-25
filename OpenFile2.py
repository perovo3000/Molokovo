import pickle

name = input(" Input File name ")
# name = name + '.txt'
print(name)

spisok = 'sdvsldvlskv'
# открываем файл для простой записи ( w,r )
with open(name, 'w+') as open_file:
    # записываем список
    open_file.write(spisok)
with open(name, 'r') as open_file:
    spisok2 = open_file.read()

print('spisok2  ', spisok2)

# открываем файл для бинарной записи записи объекта (с pickle)(wb,rb)
# создаем список, который будем грузить в файл
spisok = []
# вводим величину списка
hight = int(input('Введите величину списк  '))
for x in range(hight):
    spisok.append(x ** 2)
print(spisok)
with open(name, 'wb+') as open_file2:
    # записываем список (Файл открыт ТОЛЬКО для записи)
    pickle.dump(spisok, open_file2)
with open(name, 'rb') as open_file2:
    # открываем файл для считывания
    spisok2 = pickle.load(open_file2)

print('spisok2  ', spisok2)
