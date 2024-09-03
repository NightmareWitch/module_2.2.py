number = int(input('Введите первое число: ' ))
number1 = int(input('Введите второе число: ' ))
number2 = int(input('Введите третье число: ' ))
if number == number1 and number1 != number2:
    print(2)
elif number == number1 and number1 == number2:
    print(3)
elif number != number1 and number1 != number2:
    print(0)