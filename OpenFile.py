import pickle

poem = '''\
        jfgjdbb
        dfhbnbn
        dfd'''
# открываем файл для ЗАПИСИ
f = open('poem.txt', 'w+')
f.write(poem)
# закрываем файл
f.close()
# открываем файл для ЧТЕНИЯ
f = open('poem.txt', 'r')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line)

# pickle  - импорт и возврат любого бинарного файла
name = 'frutiz.data'
binfile = ['mango', 'banana', 'apples']
# wb - запись любого бинарного файла
f = open(name, 'wb')
pickle.dump(binfile, f)
f.close()
del binfile
f = open(name, 'rb')
binfile2 = pickle.load(f)
print(binfile2)
