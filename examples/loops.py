def knock_name(name):
    for i in range(3):
        print(f'{name}!', end='***')
    print()


def knock(number):
    while number:
        print(number)
        number -= 1
    print('the end function')


def knock_name2(counter, name):
    while counter:
        print(f'{name}!')
        counter -= 1
    print('the end function')



def loop_with_break(number):
    while number:
        print(number)
        number -= 1
        if number == 5:
            break
    print('break loop')


def loop_with_continue(number):
    while number:
        number -= 1
        if number % 2:
            continue
        print(number)
    print('continue loop')


if __name__ == '__main__':
    knock_name('Zocha')
    knock(3)
    knock_name2(4, 'Krycha')
    loop_with_break(10)
    loop_with_continue(10)