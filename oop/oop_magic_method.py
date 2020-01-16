import collections
# from collections import namedtuple # użycie tego nie wymaga uzycia collections.namedtuple(), a samego namedtuple
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits # znak _ informuje że pole jest prywatne
                       for rank in self.ranks ]
    """
     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
     suits = 'spades diamonds clubs hearts'.split()
     for suit in suits:
        for rank in ranks:
            print(Card(rank, suit))
    """

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]
    """
     Dobrze mieć min. metodę __repr__ ponieważ jeśli metoda __str__ nie istnieje
     to __repr__ zostanie wykorzystana w jej miejsce.
    """
    def __repr__(self):
        return f'Ilość kart z __repr__ {self.__len__()}'

    # def __str__(self):
    #     return f'Ilość kart z __str__ {self.__len__()}'

if __name__ == '__main__':
    print(FrenchDeck.suits) # tworzy liste stringow ze stringu po spacji
    deck = FrenchDeck()
    print(deck._cards) # tak nie robimy pole jest prywatne
    print(len(deck))
    print(deck[0], deck[12], deck[-1])
    print(choice(deck)) # wylosowanie karty
    print(deck[:3])
    print(deck[9:13])
    print(deck[9:16:2])
    print(list(reversed(deck._cards)))
    print(Card('2', 'hearts') in deck)
    print(Card('1', 'hearts') in deck)
    print(deck) # bez metody __str__ jest blad: print(deck) TypeError: __str__ returned non-string (type list)






