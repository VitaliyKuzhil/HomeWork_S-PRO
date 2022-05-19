class CustomError(Exception):
    """Use this, for my program when text_input < NULL"""


def input_digit():
    try:
        text_input = int(input('Enter your Integer: '))
        if text_input < 0:
            raise CustomError
        return text_input
    except ValueError:
        print('You must enter Integer')
        return input_digit()
    except CustomError:
        print('You enter Integer must by POSITIVE')
        return input_digit()


def fib_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib_list(n: int) -> list:
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n > 1:
        my_fib_list = [0, 1]
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
            my_fib_list.append(b)
        return my_fib_list


digit = input_digit()

numbers = fib_generator(digit)
print(f'fib_generator: ', end='')
for i in numbers:
    print(i, end=' ')
print()

print(f'fib_list: {fib_list(digit)}')

# 3) Визначити функцію-генератор fib_generator(n), яка приймає кількість елементів послідовності Фібоначчі
# та ітерується за елементами послідовності.
#
# наприклад fib_generator(3) створить ітератор для 3 елементів послідовності 0 1 1
#
# Числа Фібоначчі — елементи числової послідовності
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 46 17711, …,
# в якій перші два числа дорівнюють 0 і 1, а кожне наступне число дорівнює сумі двох попередніх чисел
#
# Написати подібну ф-ю fib_list(n), яка повертає список з елементами послідовності.
#
# Виклик ф- та fib_list(3) поверне список [0, 1, 1]
