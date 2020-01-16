dict1 = {'A': 1, 'B': 2, 'E': 3, 'G': 4}
print(dict1)
print(dict1['B'])
a = dict1.values()
print(list(a))
print(dict1.popitem())
print(dict1.pop('B'))
print(dict1)
dict1.update({'new': 2})
add_dict = {'V': 44, 'X': 33}
dict1.update(add_dict)
print(dict1)
dict1['C'] = 99
print(dict1)

dict1 = {'A': 1, 'B': 2, 'E': 3, 'G': 4}
print(dict1.fromkeys('B', 9))  # nie wiadomo co robi
dict1['B'] = 9
print(dict1)
dict2 = {}
print(dict2)
new_dict = dict(one=1, two=2)
print(new_dict)
print(dict1.get('E'))
print(dict1.get('K')) # uzycie get zwroci None jesli klucza nie ma, a nie blad
print(dict1.get(''))


"""
https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists
"""
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)

