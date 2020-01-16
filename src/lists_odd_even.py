def lists_odd_or_even(list):
    if list[0] % 2 == 0:
        return list[::2]
    elif list[0] % 2 != 0:
        return list[::2]


if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lists_odd_or_even(list1))
    print(lists_odd_or_even(list2))