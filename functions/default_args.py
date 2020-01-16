"""
 W Pythonie funkcja może posiadać domyślne argumenty.
● W takim przypadku w sygnaturze funkcji, możemy wymieniając argumenty dać znak równości i podać
domyślny argument.
● Argumenty bez domyślnych wartości muszą poprzedzać argumenty z wartościami domyślnymi, nie można
mieszać tych dwóch rodzajów.
● Wywołując funkcję można ograniczyć się do podania parametrów, które nie mają domyślnych wartości albo
podać również te, które taką domyślną wartość posiadają aby ją nadpisać.
"""
from textwrap import wrap


def format_phone_number(number, area_code='+48', delimiter='-'):
    wrapped_number = delimiter.join(wrap(number, 3))
    return f'{area_code} (0) {wrapped_number}'


if __name__ == '__main__':
    print(format_phone_number('123456789'))
    print(format_phone_number("123123123", delimiter=" "))
    print(format_phone_number(number="111111111", delimiter=":",
                              area_code="+12"))  # podanie argumentów w wywołaniu zwiększa czytelność kodu

    arguments = ("123456789",)  # ponizej *arguments przyjmuje tuple stąd ,
    print(format_phone_number(*arguments))
    keyword_arguments = {"number": "123456789", "area_code": "+48", "delimiter": "_"}
    print(format_phone_number(**keyword_arguments))

    positional_data = ['987456123', '+99', '::']
    print(format_phone_number(*positional_data))
    key_words = {'number': '654231897', 'area_code': '+00', 'delimiter': '//'}
    print((format_phone_number(**key_words)))
