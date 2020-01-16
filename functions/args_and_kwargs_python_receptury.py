"""
Dygresja do Python Receptury rozdz. 7.1 str. 203
odp. https://stackoverflow.com/questions/54115906/capturing-the-values-from-dict-items/54115921
"""
import html


def make_element(name, value, **attrs):
    print(attrs.items())
    # keyvals = [' %s="%s"' % item for item in attrs.items()] # old style
    # keyvals = [' {}="{}"'.format(*item) for item in attrs.items()] # new style
    keyvals = [f' {item[0]}="{item[1]}"' for item in attrs.items()]  # new style
    print(keyvals)
    attr_str = ''.join(keyvals)
    print(attr_str)
    element = '<{name}{attrs}>{value}</{name}>'.format(name=name,
                                                       attrs=attr_str,
                                                       value=html.escape(value))
    return element


if __name__ == '__main__':

    print(make_element('item', 'Albatros', size='large', quantity=6, dupa=1, dupa2=2))

    print('******************')
    dict1 = {'a': 1, 'b': 2}
    for item in dict1.items():
        k, v = item
        print(k)
        print(v)
        print(item)
        print('%s = %s' % item)
    print("%s=%s" % ('size', 'large'))
    tup1 = list(dict1.items())
    print(tup1[0])

    print('%(language)s has %(number)03d quote types.' % \
          {"language": "Python", "number": 2})
