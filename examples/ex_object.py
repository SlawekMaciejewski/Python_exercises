"""
Stwierdzenie, że zmienna a przechowuje wartość, mimo że w zasadzie poprawne, nie oddaje całej prawdy.
Wartość jest w Pythonie obiektem przechowywanym w pamięci, a zmienna jedynie umożliwia dostęp do niego.
 Ideę tę dobrze ilustruje schemat:
                                zmienna ------> wartość
Dwie lub więcej zmiennych może reprezentować ten sam obiekt. Mówimy o nich, że są tożsame.

Tożsamość jest warunkiem znacznie silniejszym niż równość. O obiektach równych możemy powiedzieć, że są takie same,
 czyli że przyjmują takie same wartości. Obiekty tożsame są istocie tym samym obiektem.

Dwie zmienne reprezentują dwa różne obiekty
                                a ------> wartość
                                b ------> wartość
Dwie zmienne reprezentują ten sam obiekt
                            a ------> wartość <------ b
Do sprawdzania tożsamości obiektów służy operator is. Istnieje też operator is not będący jego zaprzeczeniem.

a == b 	# sprawdza równość obiektów (czy zmienne mają te same wartości)
a is b	# sprawdza identyczność obiektów (czy zmienne są tym samym obiektem w pamięci)
a is not b	# sprawdzenie, czy dwie wartości reprezentują dwa różne obiekty
# uwaga: a is not b nie jest tym samym, co a is (not b)
"""
a = 1000
b = a
print(a == b)
print(a is b)
c = 2000.0
d = 2000.0
print(c == d)
print(c is d)
e = 'ala ma kotaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa i psaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
g = 'ala ma kotaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa i psaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
print(e == g)
print(e is g)

print('*****************')

a = 'Ala'
b = 'As'
c = a + ' i ' + b
d = 'Ala i As'
print(c == 'Ala i As')
print(c == d)
d = c
print(c is 'Ala i As')
print(c is d)

print('*****************')

a = [1,2,3]
b = a
print(a == b)
print(a is b)
c = [1,2,3]
print(a == c)
print(a is c)
a[1] = 99
print(a is b)
print(b)
b = c
print(a is c)
print(b is c)
print(b, c)

print('*****************')

dane = [[0,0]]*5 # dla podania listy jako [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]] nie zajdzie tożsamość dla poszczególnych
                 # elementów listy [0, 0]
print(dane)
# [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
print(dane[0] is dane[1])
# True
dane[0][0] = 1.0	# uwaga!
print(dane)
# [[1.0, 0], [1.0, 0], [1.0, 0], [1.0, 0], [1.0, 0]]