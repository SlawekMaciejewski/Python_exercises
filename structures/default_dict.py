from collections import defaultdict
from typing import DefaultDict


def count_letters(text: str) -> dict:
    counter = {}
    for letter in text:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter


def count_letters_defaultdict(text: str) -> DefaultDict:
    counter = defaultdict(int)
    for letter in text:
        counter[letter] += 1
    return counter


def grouping_labels(pairs_list: list) -> dict:
    new_list = {}
    for k, v in pairs_list:
        if k not in new_list:
            new_list[k] = [v]
        else:
            new_list[k].append(v)
    return new_list




def grouping_labels_defaultdict(pairs_lists: list) -> defaultdict:
    new_list = defaultdict(list)
    print(new_list)
    for k, v in pairs_lists:
        new_list[k].append(v)
    return new_list


if __name__ == '__main__':
    text1 = "Ala ma kota i Ala ma psa"
    pairs = [('yellow', 1), ('black', 2), ('yellow', 3), ('green', 5), ('green', 6), ('black', 9)]
    print(grouping_labels(pairs))
    print(grouping_labels_defaultdict(pairs))
    print(count_letters(text1))
    print(count_letters_defaultdict(text1))
    print(count_letters_defaultdict(text1)['A'])
    print(count_letters_defaultdict(text1).get('a'))
    print(count_letters_defaultdict(text1).keys())
    print(count_letters_defaultdict(text1).items())
