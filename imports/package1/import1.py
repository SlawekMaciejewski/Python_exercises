class Klasa1:
    print('Klasa1')

    def __init__(self):
        self.a = 10
        self.b = 20
        print('init1')
        print(f'init1 name: {__name__}')

    def sums(self, a, b):
        print('metoda sums1')
        return a + b
print(f'First Module\'s name: {__name__}')

if __name__ == '__main__':
    obiekt = Klasa1()
    print(obiekt.sums(3, 2))
    print(__name__)
else:
    print(f"Run from import: {__name__}")
