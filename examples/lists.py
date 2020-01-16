my_list = [1, 2, 3, 4]
my_list2 = [1, 'ala', 'ma', 2, 'koty']
my_list3 = [[1, 2, 'ala'], 5, 'Arek', (8, 9), ('pies', 6)]
my_list4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
not_sorted = [3, 2, 1, 9, 7, 8, 4, 5, 10, 6, 11]

print(my_list[2])
print(my_list)
print(my_list2)
print(my_list3)

my_list.append(11)
my_list2.append('i psy')
my_list3.append([12, 14])
my_list3.append((22, 33, 'dupa'))

print("*********list*************")

print(my_list)
print(my_list2)
print(my_list3)
print(my_list4)

print("***************************")
print(min(my_list4))
print(max(my_list4))
print(len(my_list4))
print(sum(my_list4))
print(list(reversed(my_list4)))
print(not_sorted)
print(sorted(not_sorted))
print(not_sorted)
print(not_sorted.sort()) # none
print(not_sorted)
print(my_list4)
print(not_sorted)
print(list(zip(my_list4, not_sorted)))
print(5 in my_list4) # TRUE, uzycie in sprawdza czy dany element jest na liscie
print(my_list4.index(5, 0, 5)) # zwraca indeks dla 5 i przeszukje indeksy od 0 do 5-1
# print(my_list4.index(55)) # zwroci ValueError: 55 is not in list
del my_list4[2]
print(my_list4)


# a = my_list3.pop(5)
# print(a)
# print(my_list3)
# print(my_list2[2])
# print(my_list3[1:3])
# print(my_list3[1:-1:2])  # from index 1 to -1 step 2
# print('revers', my_list3[::-1])  # revers
# print('revers', my_list3[-1:0:-1])  # revers
# print(my_list3[::-2])
# print(my_list3[0:-1])  # bez ostatniego elementu
# print(my_list4[::-2])
# print(my_list4[8:0:-2])
# print(my_list4[1::2])  # z ostatnim elementem
# new_list = my_list + my_list4
# print(new_list)
# my_list.extend(my_list4)
# n = my_list
# print(n)
# del n[5]
# print(n)

"""
https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
"""
list(range(3, 6))            # normal call with separate arguments
args = [3, 6]
print(list(range(*args)))            # call with arguments unpacked from a list




