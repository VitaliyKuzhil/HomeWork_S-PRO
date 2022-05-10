def concatenation():
    print('Input Two STR for concatenation')
    return input() + input()


print('RESULT:', concatenation())


def multiplication():
    summa = 1
    while True:
        print('Input Two INT for multiplication')
        digit = int(input())
        if digit != 0:
            print(f'{summa} * {digit} = {summa * digit}')
            summa *= digit
        else:
            print(f'{summa} * {digit} = {summa * digit}')
            break
    return summa


multiplication()

# Завдання 3
#
# Напишіть програму, в якій викликається функція, що запитує із введення
# два рядки та повертає в програму результат їх конкатенації.
# Виведіть результат на екран.
#
# Напишіть функцію, яка зчитує з клавіатури числа та перемножує їх
# доки не буде введено 0. Функція повинна повертати
# отриманий твір. Викличте функцію та виведіть на екран результат
# її роботи.