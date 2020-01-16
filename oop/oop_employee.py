import datetime


class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        # self.email = f'{first}.{last}@aptor.com' # uzywajac @property mozemy zrezygnowac z tego atrybutu

    @property
    def email(self):
        return f'{self.first}.{self.last}@aptor.com'

    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, name: str):
        self.first, self.last = name.split()

    @full_name.deleter
    def full_name(self):
        self.first = None
        self.last = None

    def applay_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, new_raise_amount):
        cls.raise_amount = new_raise_amount

    @staticmethod
    def is_workday(day):
        return day.weekday() is not (5, 6)


if __name__ == '__main__':
    employee1 = Employee('Jan', "Nowak", 100)
    employee2 = Employee('Anna', "Kowalska", 150)
    # print(employee1.full_name()) # po wprowadzeniu @property nie wywolujemy funkcji z () tylko bez jak atrybut
    # print(employee2.full_name()) # takie wywołanie jest ponizej
    print(employee1.full_name)
    print(employee2.full_name)
    print(employee1.email)
    print(employee2.email)
    print(f'{employee1.first} ', employee1.pay)
    print(f'{employee2.first} ', employee2.pay)
    employee1.applay_raise()
    print(f'{employee1.first} ', employee1.pay)
    employee2.raise_amount = 1.1  # modyfikacja atrybutu klasowego dla konkretnego obiektu
    employee2.applay_raise()
    print(f'{employee2.first} ', employee2.pay)
    print(f'{employee1.first} ', employee1.raise_amount)
    print(f'{employee2.first} ', employee2.raise_amount)
    print('z klasy ', Employee.raise_amount)
    print('*************************')
    Employee.set_raise_amount(1.1)
    print(f'{employee1.first} ', employee1.raise_amount)
    print(f'{employee2.first} ', employee2.raise_amount)
    print('z klasy ', Employee.raise_amount)
    employee1.set_raise_amount(
        1.2)  # wywołanie metody klasowej przez obiekt zmieni atrybut klasowy dla wszystkich nowych obiektów
    print(f'{employee1.first} ', employee1.raise_amount)
    print(f'{employee2.first} ', employee2.raise_amount)
    print('z klasy ', Employee.raise_amount)
    today = datetime.date.today()
    print('Is workday?', employee1.is_workday(today))
    print('Is workday?', Employee.is_workday(today))
    employee1.full_name = 'Agnieszka Mróz' # dzieki uzyciu dekoratora @atrybut.setter można przypisać fuulname do obiektu.
    print(employee1.full_name)
    print(employee1.first)
    print(employee1.email)
    del employee1.full_name
    print(employee1.full_name)
    print(employee1.email)