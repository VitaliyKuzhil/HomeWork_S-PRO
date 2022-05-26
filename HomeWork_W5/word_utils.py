import string


def clear_punctuation_marks(clear_chars):
    for character in string.punctuation:
        clear_chars = clear_chars.replace(character, '')
    return clear_chars


def get_list(chars):
    list_chars = clear_punctuation_marks(chars).split()
    return list_chars


def get_max_len_char(char):
    max_len_char = max(get_list(char), key=len)
    return max_len_char
