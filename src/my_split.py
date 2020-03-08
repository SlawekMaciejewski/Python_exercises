def my_split(text: str, sep: str = ' ') -> list:
    text = text.strip()
    split_list = []
    indx_list = []

    for i, char in enumerate(text):
        if char == sep:
            indx_list.append(i)

    split_list.append(text[:indx_list[0]])

    k = 0
    for indx in indx_list:
        if k < text.count(sep) - 1:
            split_list.append(text[indx + 1:indx_list[k + 1]])
        k += 1

    split_list.append(text[indx_list[-1] + 1:])

    return split_list



if __name__ == "__main__":
    text = '  a cc bb dd sss jjjj kkkkk  '
    print(my_split(text))
    print(text.split())