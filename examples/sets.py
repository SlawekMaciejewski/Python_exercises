my_set = {5, 3, 4, 2, 2, 5, 5, 4}
my_set2 = {7, 1, 2, 2, 3, 3, 4, 4, 4}

print('my_set', my_set)
print('my_set2', my_set2)
list_duplicate = [1, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6]
list_without_duplicate = list(set(list_duplicate))
print(list_without_duplicate)
my_set.remove(2)
print('my_set.remove(2)-->', my_set)
my_set.discard(5) # działa tak samo jak remove()
print('my_set.discard(5)-->', my_set)

my_set = {5, 3, 4, 2, 2, 5, 5, 4}
my_set2 = {7, 1, 2, 2, 3, 3, 4, 4, 4, 8}
my_set3 = {1, 2, 3}
my_set4 = {1, 2, 3}
print('my_set', my_set)
print('my_set2', my_set2)
print('my_set3', my_set3)
print('my_set4', my_set4)
print('my_set | my_set2', my_set | my_set2)  # union suma dwóch zbiorów
print('my_set2 - my_set', my_set2 - my_set)  # zwróci tylko te elementy z my_set2 których nie ma w my_set
print('my_set - my_set2', my_set - my_set2)  # zwróci tylko te elementy z my_set których nie ma w my_set2
print('my_set3 - my_set4', my_set3 - my_set4)  # zwróci set()
print('my_set3 | my_set4', my_set3 | my_set4)  # union suma dwóch zbiorów
print('my_set & my_set2', my_set & my_set2)  # zwróci czesc wspolna
print('my_set ^ my_set2', my_set ^ my_set2)  # zwróci te elementy które są różne w obu zbiorach
my_set3.add(4)
print(my_set3)
my_set3.update(my_set2)
print(my_set3)
my_set3.clear()
print(my_set3)
new_set = set()  # tworzy pusty zbiór, uzycie {} dałoby pusty słownik- dict
print(new_set)
print(len(my_set3))
print(len(my_set2))
print(my_set2)
print(sum(my_set2))

dziecko = {'a', 'c', 't', 'g'}
print('a' in dziecko)  # True
a = 'hellllooooo ggggodddd'
print(set(a))
set5 = {1, 2, 3, 4, 5, 6, 7}
set6 = {3, 4, 5}
print(set6.issubset(set5))
print(set5.issuperset(set6))
