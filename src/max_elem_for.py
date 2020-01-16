def my_max(sequence):
    largest = 0
    for element in sequence:
        if element > largest:
            largest = element
    return largest

if __name__ == '__main__':
    my_list = [11, 333, 111, 44, 5, 444, 322, 555, 6]
    largest = my_max(my_list)
    print(largest)