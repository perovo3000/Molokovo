def import_list(name):
    l = name
    return l


a = [1, 2, 3, 4, 5, 6, 7, 8, 8]
b = []
for i in a:
    b.append(i ** 2)
c = import_list(b)
print(c)
# возврат функцией списка и его печать