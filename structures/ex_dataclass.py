from dataclasses import dataclass


@dataclass(frozen=True)
class UserData:
    name: str
    surname: str
    age: int


if __name__ == '__main__':
    user = UserData('Slawek', 'Nowak', 33)
    print(user)
    print(user.age)
    user.age = 20 # dla frozen=True będzie błąd bo klasa staje się immutable jak tuple
    print(user.age)
