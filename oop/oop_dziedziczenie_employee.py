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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, programming_language):
        super().__init__(first, last, pay)
        self.programming_language = programming_language


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = set()
        else:
            self.employees = set(employees)

    def add_employee(self, employee):
        self.employees.add(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)

    def print_employes(self):
        for employee in self.employees:
            print(employee.full_name)



if __name__ == '__main__':
    wisniewska = Employee('Anna', 'Wiśniewska', 6000)
    kowalski = Employee('Emil', 'Kowalski', 8000)
    nowak = Developer('Jan', 'Nowak', 10000, 'Java')
    dlugosz = Developer('Marek', 'Długosz', 9000, 'Python')
    klich = Manager('Darek', 'Klich', 15000, {wisniewska, kowalski, nowak, dlugosz})
    klich.print_employes()
    print('*************')
    michalska = Employee('Nina', 'Michalska', 5000)
    klich.add_employee(michalska)
    klich.print_employes()
    print('*************')
    klich.remove_employee(dlugosz)
    klich.print_employes()
    nowak.applay_raise()
    print(nowak.pay)


