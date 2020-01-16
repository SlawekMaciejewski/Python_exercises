a = 0 # insert 1 or 0 to test 'if'
b = 1 # insert 1 or 0 to test 'if'
if a:
    print('a is true')
elif not a: # insert 'not' or not before 'a' if you want to test 'elif'
    print('elif: a')
elif b:
    print('elif: b')
else:
    print('else')
