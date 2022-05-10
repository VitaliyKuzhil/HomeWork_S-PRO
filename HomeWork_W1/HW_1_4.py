my_srt = input()
count_upper = 0
count_lower = 0

for i in my_srt:
    if i.isupper():
        count_upper += 1
    else:
        count_lower += 1

if count_upper > count_lower:
    print(my_srt.upper())
elif count_upper == count_lower or count_upper < count_lower:
    print(my_srt.lower())

# Завдання 4
#
# Вводиться рядок, що включає малі та великі літери.
# Потрібно вивести той самий рядок в одному регістрі, який залежить від
# того, яких літер більше. При рівній кількості перетворити на нижній
# регістр. Наприклад, вводиться рядок "HeLLo World", він має бути
# перетворена на "hello world", тому що у вихідному рядку малих літер
# більше. У коді використовуйте цикл for, рядкові методи upper()
# (перетворення до верхнього регістру) та lower() (перетворення до
# нижньому регістрі), а також методи isupper() та islower(), що перевіряють
# регістр рядка або символ.
