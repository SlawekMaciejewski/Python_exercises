scores = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, }


def scrabble_score(word: str):
    # total_score = 0
    # for letter in word.lower():
    #     total_score += scores[letter]
    # return total_score
    print([scores[letter] for letter in word]) # tworzy liste scores, ktora ponizej funkcja sum() sumuje
    return sum([scores[letter] for letter in word])  # uzycie list comprehension skraca to co powyzej


if __name__ == '__main__':
    while True:
        my_word = input('Provide word: ')
        score = scrabble_score(my_word)
        print(f'For word {my_word}. Your scores are {score}')
        shall_continue = input('Do you want to continue y/n? ')
        if shall_continue.lower() != 'y':
            break
