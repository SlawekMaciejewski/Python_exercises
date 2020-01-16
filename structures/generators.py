def gen_():
    yield 1
    yield 2
    yield 3

def gen():
    for i in range(10):
        yield i


if __name__ == '__main__':
    gen1 = gen_()
    # print(list(gen1))  # użycie tej linni spowoduje zużycie generatora i np: for się już nie wykona
    # print(list(gen1)) # zwróci pustą liste gdyz generator zuzyl sie linie wczesniej

    print(next(gen1))  # metoda next jest wywoływana aby uzyskać kolejny element z generatora tak działa for az do Stopieration
    print(next(gen1))
    print(next(gen1))

    print('//////////////////////')

    gen2 = gen()
    print(next(gen2))
    print(next(gen2))  # dla for zostanie o 2 generatroy mniej
    print('****************')
    for i in gen2:
        print(i, 'from for')
