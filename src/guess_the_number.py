from random import randint


def draw_a_number():
    random_number = randint(1, 100)
    return random_number


def is_a_number(data):
    try:
        if data.isdigit():
            return True
        else:
            data = int(data)
    except ValueError:
        print("It's not an integer, enter the correct number ")
        return False


if __name__ == "__main__":
    random_number = draw_a_number()
    # print(random_number)
    count = 0
    while True:
        count += 1
        user_number = str(input('Guess number 1 to 100, enter a integer: ').strip())
        if not is_a_number(user_number):
            continue
        if int(user_number) == random_number:
            print(f'You guessed!!! This number is: {random_number}. You guessed it {count} times')
            answer = input('Do you try again? \nPress "Y/y"(yes) or any key to (no) : ').strip()
            if answer.upper() == 'Y':
                random_number = draw_a_number()
                # print(random_number)
                continue
            else:
                break
        elif int(user_number) < random_number:
            print('The number is too small')
            continue
        elif int(user_number) > random_number:
            print('The number is too big')
            continue

