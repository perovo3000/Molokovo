import json

text = 'If it very importent, we well do it'
text_line = text.split()
for i in text_line:
    print(i)

file_name = input('Input File name  ')
file_name = file_name + ".json"
with open(file_name, 'w') as file_open:
    json.dump(text_line, file_open)
with open(file_name,'r') as file_open:
    ob =json.load(file_open)
print(ob)
