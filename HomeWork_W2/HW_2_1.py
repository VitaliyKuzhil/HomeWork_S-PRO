school = {'1а': 12, '1б': 16, '2а': 24, '2б': 18, '2в': 9}

print(f'Old DICT: {school}')

school['2а'] = 21  # update value '2a'
school['3а'] = 34  # add items '3a': 34
school.pop('2в')  # delete '2в': 9

print(f'New DICT: {school}')
print(f'All children: {sum(school.values())}')  # sum all children in school


def get_set_test(dic):  # reverse key, value and return new_school_dict
    new_school_dict = dict((value, key) for key, value in dic.items())
    return new_school_dict


result = get_set_test(school)  # address to function get_set_test

print(f'Old DICT: {school}')
print(f'New DICT: {result}')

# Завдання 1
#
# Створіть словник, зв'язавши його зі змінною school, та наповніть даними,
# які б відображали кількість учнів у різних класах (1а, 1б, 2б,
#
# 6а, 7в тощо). Внесіть зміни до словника згідно наступному:
# а) у одному з класів змінилася кількість учнів,
# б) у школі з'явився новий клас (додайте новий клас)
# с) у школі було розформовано (віддалено) інший клас.
#
# Обчисліть та виведіть загальну кількість учнів у школі.
#
# Напишіть функцію, яка приймає один словник і повертає інший,
# у якому ключами є значення першого словника, а значеннями –
# відповідні їм ключі. Створіть словник, передайте його в функцію.
#
# Виведіть на екран вихідний та "перевернутий" словники.
