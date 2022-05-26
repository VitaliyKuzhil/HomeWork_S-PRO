from contextlib import contextmanager

read_file_name = input('Input file name for read: ')
write_file_name = input('Input file name for write: ')


@contextmanager
def file_open(path, mode):
    try:
        file_obj = open(path, mode)
        yield file_obj
        print(f'File close {file_obj.closed}')
    except OSError:
        print("Exception: Invalid file NAME or PATH")
    else:
        print('Done')
    finally:
        file_obj.close()
        print(f'File close {file_obj.closed}')


with file_open(read_file_name, 'r') as read_file:
    with file_open(write_file_name, 'w') as write_file:
        count_lines = 0
        for present_line in read_file:
            count_lines += 1
            write_file.write(f'{count_lines}: {present_line}')


# 1) Напишіть програму, яка зчитуватиме вміст файлу, додавати до лічених рядків порядковий номер
# і зберігати їх у такому  вигляді в новому файлі. Ім'я вихідного файлу необхідно запросити в користувача,
# як і ім'я цільового файла. Кожен рядок у створеному  файлі повинен починатися з його номера, двокрапки та пробілу,
# після чого  має йти текст рядка з вихідного файлу.
