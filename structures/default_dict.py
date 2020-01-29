from collections import defaultdict


def count_letters(text: str) -> dict:
    counter = {}
    for letter in text:
        if letter not in counter:
            counter[letter] = 1
        else:
            counter[letter] += 1
    return counter


def count_letters_defaultdict(text: str) -> dict:
    counter = defaultdict(int)
    for letter in text:
        counter[letter] += 1
    return counter



if __name__ == '__main__':
    text1 = "Ala ma kota i Ala ma psa"
    print(count_letters(text1))
    print(count_letters_defaultdict(text1))
    print(count_letters_defaultdict(text1)['A'])
    print(count_letters_defaultdict(text1).get('a'))
    print(count_letters_defaultdict(text1).keys())
    print(count_letters_defaultdict(text1).items())
