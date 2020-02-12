if __name__ == '__main__':
    my_lambda = lambda x:  x.upper()
    print(my_lambda('map, reduce, ﬁlter'))
    square_lambda = lambda x: x**2
    print(square_lambda(3))
    equels_lambda = lambda x, y: x == y
    print(equels_lambda(2, 2))
    print(equels_lambda(2, 3))