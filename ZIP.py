import os
import time
# работа Pyton с операционной систеой
# программа создания и запуска ZIP файла

# создвние пути  файла который бэкапится
source = input("Введте путь  ")

# создание каталога куда бэкапить файл, подкаталог - год и время создания
# os.sep - разделитель в операционной системе (\ для Windows)
patch_backup = 'C:\Backup' + os.sep + str(time.strftime('%y%m%d'))
print(patch_backup)

# создание имени файла для бэкапа (время создания)
name_backup = str(time.strftime('%H%M%S'))
print(name_backup)

# проверка есть ли уже создаваемый каталог, если есть каталог не создается
if not os.path.exists(patch_backup):
    # создание каталга  для бэкапа
    os.makedirs(patch_backup, mode=0o777)

print('Cоздали ', patch_backup)
# создание строчки  zip файла
zip = patch_backup + os.sep + name_backup + '.zip'
# создаем zip команду
zip_command = "zip -qr {0} {1}".format(patch_backup, source)
print(zip_command)
if os.system(zip_command) == 0:
    print('Ok')
print('zip')
