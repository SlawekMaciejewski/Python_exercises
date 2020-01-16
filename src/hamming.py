def hamming(dziecko, list1, list2):
    count1 = 0
    count2 = 0
    for number in range(len(dziecko)):
        if dziecko[number] != list1[number]:
            count1 += 1
    for number in range(len(dziecko)):
        if dziecko[number] != list2[number]:
            count2 += 1
    if count1 > count2:
        return print(f'Ojcem jest kandydat 2')
    else:
        return print(f'Ojcem jest kandydat 1')

def hamming_zip(child, father):
    result = 0
    list_dna = list(zip(child, father))
    for element1, element2 in list_dna:
        if element1 != element2:
            result += 1
    return result

if __name__ == '__main__':
    dziecko = ['a', 'c', 't', 'g']
    fat2 = ['a', 'c', 't', 'g']
    fat1 = ['a', 'a', 'g', 'g']
    hamming(dziecko, fat2, fat1)
    print(hamming_zip(dziecko, fat1))
    print('a' in dziecko)
