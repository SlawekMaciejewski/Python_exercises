"""
Przyjmujemy założenie, że celem programu jest odczyt pliku i wyświetlenie
liczby znaków znajdujących się w poszczególnych wierszach. Użycie do tego
celu listy składanej oznacza konieczność przechowywania w pamięci wszyst-
kich wierszy pliku. Jeżeli plik jest naprawdę duży lub  pracujemy  z  nigdy
niekończącym  się  gniazdem  sieciowym,  to  oparcie  rozwiązania  na  liście
składanej okaże się problematyczne. W poniższym fragmencie kodu pokaza-
łem użycie listy składanej w sposób możliwy jedynie dla niewielkich warto-
ści danych wejściowych.
"""
# Przykład 1.
import random

with open('tmp/my_file.txt', 'w') as f:
    for _ in range(10):
        f.write('a' * random.randint(0, 100))
        f.write('\n')

value = [len(x) for x in open('tmp/my_file.txt')]
print(value)

# Przykład 2.
"""
 W trakcie działania wyrażenie generatorowe nie materializuje całej se-
kwencji danych wyjściowych. Zamiast tego wyrażenie generatorowe zwraca 
iterator pobierający po jednym elemencie z wyrażenia.
Wyrażenie generatorowe jest tworzone za pomocą ujętej w nawias składni 
przypominającej listę składaną. Poniżej przedstawiłem wyrażenie generato-
rowe odpowiadające omówionemu wcześniej kodowi. Jednak wyrażenie ge-
neratorowe natychmiast oblicza iterator i nie przechodzi do przodu.
"""
it = (len(x) for x in open('tmp/my_file.txt'))
print(it)

# Przykład 3.
"""
Jeżeli  zachodzi  potrzeba,  zwrócony  iterator  może  być  przesunięty  o  jeden 
krok do przodu, aby tym samym wygenerować kolejne dane wyjściowe na 
podstawie wyrażenia generatorowego (za pomocą wbudowanej funkcji next()). 
Kod  może  wykorzystać  dowolną  liczbę  wyrażeń  generatorowych  bez  obaw 
o nadmierne zużycie pamięci przez program.
"""
print(next(it))
print(next(it))

# Przykład 4.
"""
Wyrażenia generatorowe mają jeszcze jedną ważną cechę, jaką jest możli-
wość ich łączenia. Spójrz na poniższy przykład. Iterator z poprzedniego wy-
rażenia generatorowego został użyty w charakterze danych wejściowych dla 
kolejnego wyrażenia generatorowego.
"""
roots = ((x, x ** 0.5) for x in it)

# Przykład 5.
"""
W trakcie każdego przesunięcia iteratora do przodu następuje również prze-
sunięcie wewnętrznego iteratora do przodu, co prowadzi do powstania efektu 
domino i  zapętlenia, obliczenia  wyrażeń warunkowych oraz przekazania  da-
nych wejściowych i wyjściowych.
Generatory połączone w przedstawiony powyżej sposób są w Pythonie wyko-
nywane bardzo szybko. Kiedy szukasz rozwiązania pozwalającego na wykorzy-
stanie  funkcjonalności  operującej  na  dużym  strumieniu  danych  wejścio-
wych, wyrażenie generatorowe jest najlepszym narzędziem do wykonania tego 
rodzaju zadania. Jedyna wada polega na tym, że iteratory zwracane przez wy-
rażenia generatorowe zachowują informacje o stanie. Trzeba więc zachować
ostrożność i nie używać ich więcej niż tylko jednokrotnie (patrz sposób 17.).
"""
print(next(roots))
print(next(roots))

"""
Do zapamiętania
  Lista  składana  może  sprawiać  problemy  w  przypadku  bardzo  dużych 
danych wejściowych, ponieważ zużyje wówczas zbyt dużą ilość pamięci.
  Wyrażenia generatorowe pozwalają uniknąć problemów związanych z uży-
ciem pamięci. Generują dane wyjściowe pojedynczo i zwracają iterator.
  Wyrażenia generatorowe można ze sobą łączyć. Iterator zwrócony przez 
jedno wyrażenie może być przekazany do innego wyrażenia.
  Po połączeniu wyrażenia generatorowe są wykonywane bardzo szybko. 
"""
