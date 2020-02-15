from functools import wraps


def my_deocrator(func):
    def wrapper():
        return 'Decorated --> ' + func() + ' <-- Decorated'

    return wrapper


def my_deocrator2(func):
    def wrapper(*args, **kwargs):
        return 'Decorated --> ' + func(*args, **kwargs) + ' <-- Decorated'

    return wrapper


def my_deocrator_fin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return 'Decorated --> ' + func(*args, **kwargs) + ' <-- Decorated'

    return wrapper


def hw():
    return 'Hello world!'


def hello_name(name):
    return f'Hello {name}'


def hello_two_names(name1, name2):
    return f'Hello {name1} and hello {name2}'


@my_deocrator2
def hello_name_decorator(name):
    return f'Hello {name}'


@my_deocrator_fin
def hello_name_decorator_fin(name):
    return f'Hello {name}'


if __name__ == '__main__':
    print(hw())
    print(my_deocrator(hw)())
    print(hello_name('Krzys'))
    print(my_deocrator2(hello_name)('Kuba'))
    print(hello_two_names('Aga', 'Baba'))
    print(my_deocrator2(hello_two_names)('Krycha', 'Ola'))
    print(hello_name_decorator('Slawek'))
    print(hello_name_decorator.__name__)
    print(hello_name_decorator.__module__)
    print(print.__name__)
    print(print.__module__)
    print(hello_name_decorator_fin('Darek'))
    print(hello_name_decorator_fin.__name__)
    print(hello_name_decorator_fin.__module__)
