def tag(name, *content, cls=None, **atrs):
    """Genrate one or more HTML tags"""
    if cls is not None:
        atrs['class'] = cls
        print(atrs)
        print(sorted(atrs.items()))
    if atrs:
        attr_str = ''.join(f' {attr}="{value}"'
                           for attr, value in sorted(atrs.items()))
    else:
        attr_str = ' '
    if content:
        return '\n'.join(f'<{name}{attr_str}>{c}</{name}>'
                         for c in content)
    else:
        return f'<{name}{attr_str} />'

if __name__ == '__main__':
    print(tag('br'))
    print(tag('p', 'Hello its me', 'And you?'))
    print(tag('p', 'Its funy day :)', id=33))

    print(tag('p', 'hello', 'world', cls='sidebar'))
    print(tag(content='Testing group', name='p', cls='banner'))
    print(tag('p', 'Jakis tekst', 'dodatkowy jakis tekst', content='Testing group', cls='banner', id='22'))

    numbers_info = ('753159826', '+77', '-')
    number, area_code, delimiter = numbers_info
    print(number, area_code, delimiter)
    shopping_list = ['apples', 'oranges', 'bannans']
    apples, oranges, bannans = shopping_list
    print(apples, oranges, bannans)
    quantities = [('apples', 2), ('oranges', 3), ('bannans', 4)]
    shopping_dict = {key: value for key, value in quantities}
    print(shopping_dict)

