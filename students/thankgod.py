Cal = input('Enter an operator[+ - * / % **]')
num = float(input('Enter the 1st number: '))


if Cal == "+":
    result = num1 + num2
elif Cal == "-":
    result = num1 - num2
    print(round(result, 3))
elif Cal == "*":
    result = num1 * num2
    print(round(result, 3))
elif Cal == "/":
    result = num1 / num2
    print(round(result, 3))
elif Cal == '':
    result = num1 ** num2
    print(round(result, 3))
elif Cal == "%":
    result = num1 % num2
    print(round(result, 3))
else:
    print('Invalid')

