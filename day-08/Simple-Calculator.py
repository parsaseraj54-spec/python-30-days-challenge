number1 = float(input('Enter First number: '))
number2 = float(input('Enter Second number: '))

operation = input('Choose Operation (+,-,*,/): ')

if operation == '+':
    print(number1 + number2)
elif operation == '-':
    print(number1 - number2)
elif operation == '*':
    print(number1 * number2)
elif operation == '/':
    print(number1 / number2)
else:
    print('Invalid Operation')