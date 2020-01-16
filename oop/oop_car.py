"""
oop example
"""


class Car:
    acceleration = 10

    def __init__(self, reg_number):
        self.reg_number = reg_number
        self.in_motion = False
        self.speed = 0

    def print_reg_number(self):
        print(f'Number registration is {self.reg_number} - {self.speed} km/h')

    def drive(self):
        self.in_motion = True

    def accelerate(self):
        self.speed += self.acceleration

    def stop(self):
        self.speed = 0
        self.in_motion = False


if __name__ == '__main__':
    toyota_avensis = Car('EZD 99')
    toyota_avensis.print_reg_number()
