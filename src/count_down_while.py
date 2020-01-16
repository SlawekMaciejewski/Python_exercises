def count_down(n):
    while n >= 0:
        print(n)
        n -= 1
    return 'bum'

def count_down2(n):
    while n:
        print(n)
        n -= 1
    return 'bum'

if __name__ == '__main__':
    print(count_down(10))
    print(count_down2(10))