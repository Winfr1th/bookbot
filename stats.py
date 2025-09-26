def get_num_words(file):
    num_words = file.split()
    num_words = len(num_words)
    return num_words

def char_counts(file):
    char_dict = {}
    words = file.lower()
    for char in words:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort(char_dict):
    return char_dict['num']

def sort_char(char_dict):
    new_dict = []
    for char in char_dict:
           new_dict.append({"char": char, "num": char_dict[char]})
    new_dict.sort(reverse = True, key = sort)
    return new_dict

