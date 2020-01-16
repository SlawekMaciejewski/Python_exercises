def colatz(n):
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n * 3 + 1
        else:
            n = n / 2


def colatz2(n):
    while n >= 1:
        print(n)
        if n == 1:
            return 1
        elif n % 2 == 0:
            n = n / 2
        elif n % 2 != 0:
            n = n * 3 + 1


def colatz_rek(n):
    print(n)
    if n == 1:
        return 1
    elif n % 2 != 0:
        return colatz_rek(n * 3 + 1)
    elif n % 2 == 0:
        return colatz_rek(n / 2)


if __name__ == '__main__':
    print(colatz(15))
    print(colatz2(15))
    print(colatz_rek(15))
