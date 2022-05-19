class FormulaError(Exception):
    """Use this, when the formula for my program is entered incorrectly"""


def calculator(string):
    list_str = string.split()

    try:
        if len(list_str) != 3:
            raise FormulaError

        float(list_str[0]) and float(list_str[2])

        if list_str[1] not in ['+', '-', '*', '/']:
            raise FormulaError
    except (FormulaError, ValueError):
        return 'FormulaError'
    else:
        x, y = float(list_str[0]), float(list_str[2])

        if list_str[1] == '+':
            return f'{x} {list_str[1]} {y} = {x + y}'
        elif list_str[1] == '-':
            return f'{x} {list_str[1]} {y} = {x - y}'
        elif list_str[1] == '*':
            return f'{x} {list_str[1]} {y} = {x * y}'
        elif list_str[1] == '/':
            try:
                result = x / y
                return f'{x} {list_str[1]} {y} = {result}'
            except ZeroDivisionError:
                result = "Can't divide by NULL"
                return result


print(calculator('7 + 3'))
print(calculator('10 - 2'))
print(calculator('2 * 6'))
print(calculator('12 / 4'))

print(calculator('5 . 1'))
print(calculator('7e - 2'))
print(calculator('3 * 8g'))
print(calculator('10 - 2 / 4'))

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
