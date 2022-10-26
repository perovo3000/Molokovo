# обработка исключений
try:
    text = input("ВВЕДИТЕ ТЕКСТ   ")
except EOFError:
    # если нажали Ctrl -D
    print("Зачем нажали EOF")
except KeyboardInterrupt:
    # если нажали Ctrl -C
    print('Вы отменили операцию')
else:
    print("your world is  ", text)

while True:
    # цикл будет вечен, пока не будет введен 'q'
    number_1 = input('Input first number  ')
    number_2 = input('Input second number  ')
    if number_2 == 'q' or number_1 == 'q':
        break
    try:
        number = int(number_1) / int(number_2)
    except ZeroDivisionError:
        print('Division on ZERO')
    else:
        print('Result is  ', number)
