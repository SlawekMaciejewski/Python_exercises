import re
print(re.findall(r'.\d', '12'))
print(re.search(r'ala', 'ale ola ela ala'))
print(re.search(r'.la', 'ale ola ela ala'))

print(re.findall(r'.la', 'alae ola ela ala'))
print(re.findall(r'Ala', 'alae ola ela ala'))
print(re.findall(r'Ala', 'alae ola ela ala', re.I)) # flaga re.I ignoruje wielkość liter
print(re.findall(r'#\w+', 'dupa #cycki ola #oczy'))

print(re.match(r'Ala', 'ala ola ela ala', re.I))
print(re.match(r'\w+', 'wąż'))
print(re.match(r'\w+', 'wąż', re.A))
print(re.match(r'\w+', 'wąż', re.U))
print(re.match(r'\w+', 'waz', re.A))

print(re.fullmatch(r'\w+', 'wazwaz'))
print(re.fullmatch(r'\w+', 'wąż', re.A))
print(re.fullmatch(r'\w+', 'wąż', re.U))

print(re.sub(r'\w{4}', 'psa', 'Ala ma kota i domki i ogrodek')) # zamieni kazde slowo które ma min 4 znaki na psa, pozostałe znaki zostana
print(re.sub(r'\w{4}', 'psa', 'Ala ma kota i domki i ogrodek', 2)) # zamieni kazde slowo które ma min 4 znaki na psa i tylko 2 wystapienia, pozostałe znaki zostana
print(re.sub(r'\w{4,5}', 'psa', 'Ala ma kota i domki i ogrodek')) # zamieni kazde slowo które ma min 4 znaki i max 5 na psa, pozostałe znaki zostana

print(re.subn(r'\w{4}', 'psa', 'Ala ma kota'))
print(re.subn(r'\w{4}', 'psa', 'Ala ma kota i domek')) # zwraca ile zamian przeprowadzono

it = re.finditer(r'.la', 'ola ala ela')
it.__next__() # zuzywamy jeden iterator zostanie ala i ela
for match in it:
    print(match)

"""
Przekształcenie tekstu camel case (CzyliDokłanieTak) do  ([‘Czyli’, ‘Dokładnie’, ‘Tak’])
"""
print(re.split(r'[A-Z]', 'AlaMaKota')) # to nie zadziałą, bo usunie separator każdą wielką literę
print(re.split(r'(?=[A-Z])', 'AlaMaKota'))
print(re.split(r'(?=[A-Z])', 'UPPER'))
print(re.split(r'(?<!^)(?=[A-Z])', 'XYZAlaMaKota'))
print(re.split(r'(?<=[a-z])(?=[A-Z])', 'XYZAlaMaKota'))
print(re.split(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', 'XYZAlaMaKota'))
print(re.split(r'(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])', 'UPPER'))






