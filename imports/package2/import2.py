from imports.package1.import1 import Klasa1


class Klasa2(Klasa1):
    print('Klasa2')

    def __init__(self):
        super().__init__()
        self.a = 5
        self.b = 15
        print('init2')
        print(f'init2 name: {__name__}')

    def sums(self, a, b):
        print('metoda sums2')
        return a + b
print(f'Second Module\'s name: {__name__}')

if __name__ == '__main__':
    print('nic')
    obiekt2 = Klasa2()
    obiekt1 = Klasa1()
    print(obiekt1.sums(3, 2))
    print(obiekt2.sums(4, 3))
