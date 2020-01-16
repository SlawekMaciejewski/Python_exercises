if __name__ == '__main__':

    numbers_info = ('753159826', '+77', '-')
    number, area_code, delimiter = numbers_info
    print(number, area_code, delimiter)
    shopping_list = ['apples', 'oranges', 'bannans']
    apples, oranges, bannans = shopping_list
    print(apples, oranges, bannans)
    quantities = [('apples', 2), ('oranges', 3), ('bannans', 4)]
    shopping_dict = {key: value for key, value in quantities}
    print(shopping_dict)

    a = 1
    b = 2
    print(f'a= {a}, b= {b}')
    a, b = b, a
    print(f'a= {a}, b= {b}')

    a, b, *rest = range(5)
    print(a, b, rest)
    a, *rest, b, c = range(8)
    print(a, rest, b, c)


