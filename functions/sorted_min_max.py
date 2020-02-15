if __name__ == '__main__':
    pairs = [(1, 10), (2, 9), (3, 8)]
    print(min(pairs))
    print(max(pairs))
    print(min(pairs, key=lambda x: x[1]))
    print(max(pairs, key=lambda x: x[1]))
    print(min(pairs, key=lambda x: x[0] * x[1]))
    print(max(pairs, key=lambda x: x[0] * x[1]))
    print(sorted(pairs, key=lambda x: x[1]))
    list = [1, 2, 3, 4, 5, 6, 7, 8]
    print(sorted(list, key=lambda x: x % 2 == 1))
    list2 = ['oleksandra', 'domek', 'telewizor']
    print(sorted(list2))
    print(sorted(list2, key=len))
    print(sorted(list2, key=len, reverse=True))
    print((sorted(list2, key=lambda x: x[1])))
    list2.sort() # A method modifies the list in-place
    print(list2) # list2 was change
