old_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x ** 2 for x in old_list if not x % 2]
print(new_list)


def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res


d = "Ala Ma Kota"
print(capitalize_all(d))


def capitalize_all2(t):
    return [s.capitalize() for s in d]


print(capitalize_all2(d))


def only_upper(t):
    res = []
    for s in t:
        if s.isupper(): # returned True when letter is upper case
            res.append(s)
    return res

print(only_upper(d))

def only_upper2(t):
    return [s for s in t if s.isupper()]

print(only_upper2(d))