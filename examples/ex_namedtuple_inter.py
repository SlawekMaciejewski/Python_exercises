from collections import namedtuple

NumberInfo = namedtuple('NumberInfo', 'number area_code delimiter')

pierwszy_numer = NumberInfo('1234546', '+48', '-')
print(pierwszy_numer)
print(pierwszy_numer.area_code)