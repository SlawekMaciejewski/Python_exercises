def izogram(word):
    lenght = len(word)
    my_set = set(word)
    lenght_set = len(my_set)
    if lenght != lenght_set:
        print('It is not izogram!')
    else:
        print('Is it izogram')


def izogram2(word):
    return len(word) == len(set(word))


def izogram3(word: str):
    letters = set()
    for letter in word.lower():
        if letter in letters:
            return False
        letters.add(letter)
    return True


if __name__ == '__main__':
    # word = input('Provide word: ')
    # print(izogram3(word))

    while True:
        word = input('Provide word: ').strip()
        answer = 'is' if izogram3(word) else 'is not'
        print(f' Word {word} {answer} an isogram\n')
        cont = input('Do you want continue y/n?: ')
        if cont.lower() != 'y':
            break
