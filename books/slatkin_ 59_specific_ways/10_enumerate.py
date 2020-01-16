from random import randint

# Przykład 2.
random_bits = 0
for i in range(5):  # range używamy dla iterownia się po zbiorze liczb całkowitych
    if randint(0, 1):
        random_bits |= 1 << i
        print(f'+1 dec: {random_bits}   bin: {bin(random_bits)}')
    print(f'indx loop "for" is {i} --> dec: {random_bits}   bin: {bin(random_bits)}\n')

print(random_bits, bin(random_bits))

# Przykład 2.
flavor_list = ['waniliowe', 'czekoladowe', 'orzechowe', 'truskawkowe']
for flavor in flavor_list:
    print('lody %s są wyborne' % flavor)

# Przykład 3.
for i in range(len(flavor_list)): # zła praktyka kiedy mamy kolekcję
    flavor = flavor_list[i]
    print('%d: %s' % (i + 1, flavor))

# Przykład 4.
# Funkcja enumerate() opakowuje dowolny iterator
# opóźnionym generatorem. Generator pobiera z iteratora parę — indeks pętli
# i kolejną wartość. Zmodyfikowana wersja kodu jest znacznie czytelniejsza.
for i, flavor in enumerate(flavor_list):
    print('%d: %s' % (i + 1, flavor))

# Przykład 5.
# Kod  może  być  jeszcze  krótszy  dzięki  wskazaniu  liczby,  od  której  funkcja
# enumerate() rozpoczyna odliczanie (w omawianym przykładzie jest to 1).
for i, flavor in enumerate(flavor_list, 1):
    print('%d: %s' % (i, flavor))
