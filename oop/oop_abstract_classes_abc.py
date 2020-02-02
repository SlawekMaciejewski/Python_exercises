import abc
import typing


class Instrument(abc.ABC):

    @classmethod
    def play(self):
        pass


class Guitar(Instrument):

    def play(self):
        print('brzdek, brzdek')


class Flute(Instrument):

    def play(self):
        print('fiu, fiu')


class Violin(Instrument):

    def play(self):
        print('skrzyp, skrzyp')


def conductor(instruments: typing.Sequence[Instrument]) -> None:
    for instrument in instruments:
        instrument.play()


if __name__ == '__main__':
    # instrument1 = Instrument() # nie da się stworzyc obiektu klasy abstrakcyjnej
    # instrument1.play() # TypeError: Can't instantiate abstract class Instrument with abstract methods play
    instrument2 = Guitar()
    instrument2.play()
    instrument3 = Flute()
    instrument3.play()
    instrument4 = Violin()
    instrument4.play()
    orchestra = [Guitar(), Violin(), Flute()]
    conductor(orchestra)
    conductor([instrument4, instrument3, instrument2])

