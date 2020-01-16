class Fib:
    def __init__(self, n):
        self.iteration = 0
        self.n = n
        self.current = 0
        self.next = 1

    def __next__(self):
        if self.iteration == self.n:
            raise StopIteration
        self.iteration += 1
        ret = self.current
        self.current = self.next
        self.next += ret
        return ret

    def __iter__(self):
        return self


class Fib2:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return FibIter(self.n)


class FibIter:
    def __init__(self, n):
        self.iteration = 0
        self.n = n
        self.current = 0
        self.next = 1

    def __next__(self):
        if self.iteration == self.n:
            raise StopIteration
        self.iteration += 1
        ret = self.current
        self.current = self.next
        self.next += ret
        return ret


class Iterable:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Iter(self.n)


class Iter:
    def __init__(self, n):
        self.iteration = 0
        self.n = n

    def __next__(self):
        if self.iteration == self.n:
            raise StopIteration
        self.iteration += 1
        return self.iteration


if __name__ == '__main__':
    # fib = Fib2(5)
    # fib_iter = FibIter(5)
    # for f in fib:
    #     print(f)
    # for s in fib:
    #     print(s)

    # print(next(fib_iter))
    # print(next(fib_iter))
    # print(next(fib_iter))
    # print(next(fib_iter))
    # print(next(fib_iter))
    # print(next(fib_iter))
    # print(next(fib_iter))
    iter = Iterable(3)
    for i in iter:
        print(i)

    for s in iter:
        print(s)
