def fib(f):
    """

    :param f:
    :return:
    """
    f0 = 0
    f1 = 1
    f2 = 1
    print(f0)
    print(f1)
    print(f2)
    for i in range(3, f+1):
        fn = f1 + f2
        f1 = f2
        f2 = fn
        print(fn)

def fib_list(f):
    """
    The function uses a list of Python
    :param f:
    :return:
    """
    fib_list = [0, 1]
    fn = fib_list[-2] # display F0
    print(fn)
    fn = fib_list[-1] # display F1
    print(fn)
    for i in range(1, f):
        fn = fib_list[-1] + fib_list[-2] # calculate next value numbers of Fibbonacci Fn=F0+F1
        fib_list.append(fn) # add to list next numbers
        print(fn)

def fib_rek(f):
    if f < 1:
        return 0
    if f < 2:
        return 1
    return fib_rek(f - 1) + fib_rek(f - 2)

def fib_while(f):
    """
    The function uses a loop 'while' of Python
    :param f:
    :return:
    """
    f0, f1 = (0, 1)
    print(f0)
    print(f1)
    while f+1 > 2:
        f0, f1 = f1, f0+f1
        print(f1)
        f -= 1


if __name__ == '__main__':
    f = int(input('How many numbers of Fibbonacci do you want to display: '))
    #print(type(f)) # test for type class
    #fib(f)      # Try it, turn on - Python Iteration
    fib_list(f) # Try it, turn on - Python List
    for i in range(0, f+1):# Try it, turn on - Python Recursion
        print(fib_rek(i))  # Try it, turn on - Python Recursion
    #fib_while(f) # Try it, turn on - Python Loop While

    #print(fib_rek(f))
