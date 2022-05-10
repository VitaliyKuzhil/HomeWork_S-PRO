def uni_code():
    print('Input your DIGIT for convert to UNICODE')
    digit = int(input())

    if 0 < digit <= 65533:
        print(chr(digit))
        uni_code()
    elif digit == 0:
        print('STOP')
    else:
        print('Your input DIGIT outside the table UNICODE')
        uni_code()


uni_code()


def ten_characters():
    print('Input your STR for def ten_characters')
    characters = input()

    if len(characters) <= 10:
        return f"Ten characters: {characters + '*' * (10 - len(characters))}"
    else:
        return f'Length YOUR input characters > 10 characters \n' \
               f'YOUR input 10 characters Length: {characters[:10]}'


print(ten_characters())


def min_max_test():
    print('Input your six FLOAT for def min_max_test')
    list_float = [float(input()) for _ in range(6)]

    minimum = list_float[0]
    maximum = list_float[0]

    for i in list_float:
        if i > maximum:
            maximum = i
        elif i < minimum:
            minimum = i
    print(f'Min: {"%.2f" % minimum} and Max: {"%.2f" % maximum}')


min_max_test()


# Завдання 5
#
# Напишіть програму, яка циклічно запитує у користувача номера
# символів за таблицею Unicode та виводить відповідні їм символи.
#
# Завершує роботу під час введення нуля.
#
# Напишіть програму, яка вимірює довжину введеного рядка. Якщо
# рядок довше десяти символів, то виноситься попередження. Якщо
# коротше, то до рядка додається стільки символів *, щоб його довжина
# становила десять символів, після чого новий рядок має виводитися
# на екрані.
#
# Напишіть програму, яка запитує у користувача шість
# дійсних чисел. На екран виводить мінімальне та максимальне з них,
# заокруглені до двох знаків після коми. Виконайте завдання без
# використання вбудованих функцій min() та max().
