from copy import deepcopy

slownik = {'jeden': 1, 'dwa':2, 'trzy': 3}
lista1 = [slownik, 4, 5, 6]
def zmien_liste_albo_nie(lista):
    lista[1] = 40
    lista[0]['jeden'] = 10
    print('funk', lista)
print(lista1)
zmien_liste_albo_nie(lista1[:]) # [:] przekazywana jest kopia ale plytka
print(lista1)
print('********************')
"""
http://getitjob.pl/2019/09/09/akcja-rekrutacja-python-16/
Zakładając, że zależy nam by nasza funkcja nie zmieniała prawdziwej listy należałoby użyć kopiowania głębokiego:
Teraz już mamy pewność, że pracujemy na kopii naszej listy. „deepcopy” zadba o dokładne skopiowanie wszystkich jej elementów."""

slownik = {'jeden': 1, 'dwa':2, 'trzy': 3}
lista1 = [slownik, 4, 5, 6]
def zmien_liste_albo_nie(lista):
    lista[1] = 40
    lista[0]['jeden'] = 10
    print('funk', lista)
print(lista1)
zmien_liste_albo_nie(deepcopy(lista1))
print(lista1)