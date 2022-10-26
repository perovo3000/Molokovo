import json
'''json - создание и чтение файла из итеррируемого объекта'''

text = 'If it very importent, we well do it'
# split создает итрируемый файл из текста
text_line = text.split()
for i in text_line:
    print(i)

file_name = input('Input File name  ')
file_name = file_name + ".json"
# открываем файл для записи и записываем
with open(file_name, 'w') as file_open:
    json.dump(text_line, file_open)
# открываем файл для считывания и считываем
with open(file_name,'r') as file_open:
    ob =json.load(file_open)
print(ob)
