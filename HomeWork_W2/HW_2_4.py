def get_input():
    print('Input your STR ')
    return input()


def test_input(string):
    flag = True
    if len(string) < 1:
        print('Input STR, not NONE ')
        get_input()  # 'input char, not NONE'
    else:
        for i in string:
            if i.isalpha():
                flag = False
    return flag


def str_to_int(char):
    return int(char)


def print_int(result):
    print(f'Your INT number: {result} \n Type: {type(result)} \n Id: {id(result)}')


res_get_inp = get_input()
res_test_inp = test_input(res_get_inp)

if res_test_inp is True:
    res_digit = str_to_int(res_get_inp)
    print_int(res_digit)
else:
    print("Your STR can't be convert to INT")

# Завдання 4
#
# Напишіть програму, в якій визначено наступні чотири функції:
#
# Функція getInput не має параметрів, запитує введення з клавіатури та
# повертає в основну програму отриманий рядок.
#
# Функція testInput має один параметр. У тілі вона перевіряє, чи можна
# передане їй значення перетворити на ціле число. Якщо можна,
# повертає логічне True. Якщо не можна – False.
#
# Функція strToInt має один параметр. У тілі перетворює передане
# значення до цілого типу. Повертає отримане число.
#
# Функція printInt має один параметр. Вона виводить передане значення
# на екран нічого не повертає.
#
# В основній гілці програми викличте першу функцію. Те, що вона
# повернула, передайте у другу функцію. Якщо друга функція повернула True,
# ті самі дані (з першої функції) передайте в третю функцію, а
# повернене третьою функцією значення – четверту.
