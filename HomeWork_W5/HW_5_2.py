from word_utils import clear_punctuation_marks as clear, get_list, get_max_len_char as max_char


char_input = input('Input your text: ')

print(f'Clear punctuation marks: {clear(char_input)}')

print(f'Get list: {get_list(char_input)}')

print(f'Get max len char: {max_char(char_input)}')
