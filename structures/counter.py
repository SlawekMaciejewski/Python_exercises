"""
Counter przyjmuje dowolną kolekcję (listę, krotkę, string) a jest typem słownika, którego kluczami są elementy
wejściowej kolekcji a wartościami ilości wystąpień.
Counter posiada wszystkie metody znane ze słownika jak również metodę most_common(n), zwracającą n
najczęściej występujących elementów.
"""
from collections import Counter


def count_instances(some_list: list) -> Counter:
    return Counter(some_list)


def count_instances2(some_list: list) -> dict:
    return {x: some_list.count(x) for x in set(some_list)}


def count_instances3(some_list: list) -> dict:
    my_set = set(some_list)
    my_dict = {}
    for x in my_set:
        my_dict[x] = some_list.count(x)
    return my_dict


if __name__ == '__main__':
    my_list = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]
    # print(Counter(my_list))

    print(count_instances(my_list))
    print(dict(count_instances(my_list)))
    print(list(count_instances(my_list)))
    print(set(count_instances(my_list)))
    print(count_instances(my_list).most_common(2))
    print('******************')
    print(count_instances2(my_list))
    print(count_instances3(my_list))

