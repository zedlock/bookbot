from functools import reduce
def count_words(text):
    return len(text.split())

def count_chars(text):
    def update_dict(dict, char):
        dict[char.lower()] = dict.get(char.lower(), 0) + 1
        return dict

    return reduce(
        update_dict,
        list(text),
        {}
    )

def sorted_dict_list(dict):
    dict_list = []
    for char in dict:
        dict_list.append({char: dict[char]})

    dict_list.sort(reverse=True, key=lambda dict: list(dict.values())[0])

    return dict_list
