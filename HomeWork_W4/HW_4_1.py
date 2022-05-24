class FormulaError(Exception):
    """Use this, when the formula for my program is entered incorrectly"""


list_str = input().split()


def calculator(string):
    x, y = float(string[0]), float(string[2])

    if string[1] == '+':
        return f'{x} {string[1]} {y} = {x + y}'
    elif string[1] == '-':
        return f'{x} {string[1]} {y} = {x - y}'
    elif string[1] == '*':
        return f'{x} {string[1]} {y} = {x * y}'
    elif string[1] == '/':
        return f'{x} {string[1]} {y} = {x / y}'


try:
    if len(list_str) != 3:
        raise FormulaError

    float(list_str[0]) and float(list_str[2])

    if list_str[1] not in ['+', '-', '*', '/']:
        raise FormulaError

    if list_str[1] == '/' and list_str[2] == '0':
        raise FormulaError

except (FormulaError, ValueError):
    print('FormulaError')
else:
    print(calculator(list_str))

# 1) Необхідно написати функцію калькулятор, яка приймає рядок, що складається з числа,
# оператора та другого числа розділених пробілом. Наприклад ('1+1'); Необхідно розділити рядок,
# використовуючи str.split(), і перевірити є результуючий список валідним.
#
# a) Якщо введення не складається з 3 елементів, необхідно порушити виняток FormulaError, який є винятком користувача.
#
# b) Спробуйте конвертувати перше та третє значення введення до типу float.
# Перехопіть будь-які винятки типу ValueError, що виникають, та викиньте FormulaError
#
# c) Якщо друге значення введення не є '+', '-', '*', '/' також викинете FormulaError.
#
# Якщо інпут валідний – ф-я має повернути результат операції
