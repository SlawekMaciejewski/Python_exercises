def fizz_buzz(n):
    n = int(n)
    if n % 3 == 0 and n % 5 == 0:
        return f'{n} - FizzBuzz'
    elif n % 3 == 0:
        return f'{n} - Fizz'
    elif n % 5 == 0:
        return f'{n} - Buzz'
    else:
        return n


def fizz_buzz2(num):
    out = ''
    if num % 3 == 0:
        out += 'Fizz'
    if num % 5 == 0:
        out += 'Buzz'
    if not out:
        out = num
        return out
    return f'{num} - {out}'


if __name__ == '__main__':
    for i in range(1, 31):
        print(fizz_buzz2(i))
    print(fizz_buzz('3'))
