a = 'a    ala    ma kot    '
print(a)
print(a.split()) # robi liste elementow domyslnie po spacji, wiele spacji jest traktownych jako jedna i usuwana
# string.split(separator, max) max - domyslnie -1 czyli wszystkie wystapienia
print(a.strip()) # usuwa białe znaki na początku i koncu
print(a.split(' ')) #jesli poda się separator i wystepuje on po sobie to jest traktowany jako osobny str
b = 'ala jest, mila, fajna, jest tez grzeczna'
print(b.split(sep=','))
print(b.split(sep=',', maxsplit=2))
print(b.capitalize())
print(b.upper())
print(b.count('a'))
list1= [' 1 ', ' 2 ', ' 3 ']
tup = (' i ', ' bzz ', ' cii  ')
print(b.join(list1))
print(b.join(tup))
print('*************************')
a = 'żółw'
print(a)
b = a.encode('cp1250')
print(b)
print(type(b))
wierszdanych = '1\t12.22\t\n\n-10.55\n'
wektor = wierszdanych.split()
print(wektor)
tekst = 'Adam Kowalski 2008-12-22 Wrocław'
print(tekst)
record = tekst.split()
print(record)
separator = ' '
print(separator.join(record))
zdanie = 'Ala ma Asa.'
print(zdanie.replace('A', 'O')) # zmienna orginalna zdanie nie jest zmodyfikowana
print(zdanie)
zdanie = zdanie.replace('A', 'O') # modyfikacja zmiennej orginalnej
print(zdanie)