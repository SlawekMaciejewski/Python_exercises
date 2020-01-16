# Przykład 1.
names = ['Cecylia', 'Liza', 'Maria']
letters = [len(x) for x in names]
print(letters)

longest_name = None
max_letters = 0

for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count
print(longest_name)

# Przykład 2.
longest_name = None
max_letters = 0
for i, name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)

# Przykład 3.
"""
Aby tego rodzaju kod był znacznie czytelniejszy, Python oferuje wbudowaną
funkcję zip(). W Pythonie 3 funkcja zip() stanowi opakowanie dla co naj-
mniej  dwóch  iteratorów  wraz  z  opóźnionym  generatorem.  Generator  zip() 
pobiera krotki zawierające następną wartość z każdego iteratora. W efekcie 
otrzymujemy kod znacznie czytelniejszy niż w wersji indeksującej wiele list.
"""
longest_name = None
max_letters = 0
print(list(zip(names, letters)))
print(zip(names, letters)) # w Python 3 zip() jest gneratorem, w Python2 nie bedzie to list wszystkich krotek, należy
                            # użyć funkcji izip() z itertools
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count
print(longest_name)

# Przykład 4.
"""
Dane wyjściowe nie zawierają nowego elementu dla imienia Rozalinda. Taki 
jest sposób działania funkcji zip(). Pobiera krotki aż do chwili wyczerpania 
opakowanego  iteratora.  Tego  rodzaju podejście sprawdza się  doskonale,  gdy 
iteratory mają taką samą długość, co często ma miejsce w przypadku list po-
chodnych tworzonych przez listy składane. W wielu pozostałych przypadkach 
działanie funkcji zip() polegające na skracaniu jest zaskakujące i niepożą-
dane. Jeżeli nie masz pewności, że długość list, które mają być użyte wraz 
z funkcją zip(), pozostanie taka sama, to zamiast funkcji zip() rozważ wyko-
rzystanie funkcji zip_longest() z wbudowanego modułu itertools (w Pythonie 2 
jest ona nazywana również izip_longest()).
"""
names.append('Rozalia')
for name, count in zip(names, letters):
    print(name)
