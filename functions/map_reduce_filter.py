from functools import reduce


if __name__ == '__main__':
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, items))
    print(squared)
    square_sum = reduce((lambda x, y: x + y), squared)
    print(square_sum)
    odds = tuple(filter(lambda x: x % 2, squared))
    print(odds)
    odds = tuple(filter(lambda x: x % 2, range(1, 50)))
    print(odds)