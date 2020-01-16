import numpy as np


def range_with_floats(start, stop, step):
    while stop > start:
        yield round(start, 2)
        start += step


if __name__ == '__main__':
    print(range(10))
    print(type(range(3)))
    print(list(range(10)))
    print(list(range(3, 10)))
    print(list(range(3, 20, 1)))
    print(list(range(3, 20, 2)))
    print(list(range(10, -30, -5)))
    print(list(range(0)))
    print(range(5)[2])
    print(list(range(5)[:3]))

    for i in reversed(range(5)):
        print(i)

    for i in range(17, 10):  # jeśli nie możemy osiągnąć argumentu stop, range nic nie zwróci
        print(i)
    print(list(range(17, 10)))  # jeśli nie możemy osiągnąć argumentu stop, range zwróci pustą listę

    for i in range_with_floats(1.5, 2.5, 0.1):
        print(i)

    for i in np.arange(1.5, 2.5, 0.1):
        print(round(i, 2))

