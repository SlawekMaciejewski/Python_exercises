for i in range(3):
    print('iterator:', i)
else:  # 'else' execute always when 'for' was completed !!!
    print('else')
print(i)

for i in range(3):
    print('iterator:', i)
    if i == 1:
        break  # using a 'break' statement in a loop  will actually skip the 'else' block
else:
    print('else2')

for i in []:
    print('never runs')
else:
    print('else')

while False:
    print('never runs')
else:
    print('while else')

a = 3 # to testing use 3 or 4
b = 9
for i in range(2, min(a, b) + 1):
    print('Testing', i)
    if a % i == 0 and b % i == 0:
        print('Not coprime')
        break
else:
    print('Coprime')