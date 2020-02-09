import datetime
import re


def calculate_checksum_from_pesel(pesel: str) -> int:
    weights_of_a_number = (9, 7, 3, 1, 9, 7, 3, 1, 9, 7)
    list_checksum = []
    checksum = 0
    for p, n in zip(pesel, weights_of_a_number):
        list_checksum.append(int(n) * int(p))
    print(list_checksum)
    for element in list_checksum:
        if re.match(r'\d{2}', str(element)):
            # get the last digit from number, may use int(repr(element)[-1]) or modulo
            checksum += element % 10
        else:
            checksum += element
    print(checksum)
    if checksum > 10:
        if checksum % 10 == 0:
            return 0
        else:
            return checksum % 10


def check_control_number_in_pesel(pesel: str) -> bool:
    if calculate_checksum_from_pesel(pesel) == int(re.findall(r'\d$', pesel)[0]):  # int(pesel[-1])
        return True
    else:
        return False


def born_date(date_time_str: str):
    date_time_obj = datetime.datetime.strptime(date_time_str, '%Y%m%d')
    return date_time_obj.date()


def correct_born_date(pesel: str) -> str:
    born_date_from_pesel = re.findall(r'^\d{6}', pesel)

    if re.fullmatch(r'^\d{2}[8]\d{3}', str(born_date_from_pesel[0])):
        corrected_born_date = '18' + born_date_from_pesel[0][0:2] + '0' + born_date_from_pesel[0][3:]
        return corrected_born_date
    elif re.fullmatch(r'^\d{2}[9]\d{3}', str(born_date_from_pesel[0])):
        corrected_born_date = '18' + born_date_from_pesel[0][0:2] + '1' + born_date_from_pesel[0][3:]
        return corrected_born_date
    elif re.fullmatch(r'^\d{2}[2]\d{3}', str(born_date_from_pesel[0])):
        corrected_born_date = '20' + born_date_from_pesel[0][0:2] + '0' + born_date_from_pesel[0][3:]
        return corrected_born_date
    elif re.fullmatch(r'^\d{2}[3]\d{3}', str(born_date_from_pesel[0])):
        corrected_born_date = '20' + born_date_from_pesel[0][0:2] + '1' + born_date_from_pesel[0][3:]
        return corrected_born_date
    else:
        if re.fullmatch(r'^\d{2}[01]\d{3}', str(born_date_from_pesel[0])):
            corrected_born_date = '19' + born_date_from_pesel[0][0:]
            return corrected_born_date
        else:
            print('Unknown born date')
            return '00000000'


def validate_the_length_of_the_PESEL(pesel: str) -> bool:
    try:
        if re.fullmatch(r'^\d[0]{10}$', pesel):
            raise Exception
        elif re.fullmatch(r'\d{4}[0123]\d{6}', pesel):
            return True
        else:
            raise Exception
    except Exception:
        print(
            "Wrong the length of the PESEL or length must be exactly 11 digits or PESEL must contain only digits or "
            "others rules don't match.")
        return False


def is_woman(pesel: str) -> bool:
    if re.fullmatch(r'^\d{9}[02468]\d{1}', pesel):
        return True
    else:
        return False


if __name__ == '__main__':
    while True:
        pesel1 = input('Provide the PESEL: ').strip()
        print('You provided the PESEL: ', pesel1)
        if not validate_the_length_of_the_PESEL(pesel1):
            continue
        elif not check_control_number_in_pesel(pesel1):
            print("The PESEL is wrong provide again")
            continue
        # 12831567894 12921567896 12221567895 12321567898 12021567899 12121567892
        elif is_woman(pesel1):
            print(f'Your PESEL is {pesel1}, you are a woman and you were born in {born_date(correct_born_date(pesel1))}.')
            break
        else:
            print(f'Your PESEL is {pesel1}, you are a man and you were born in {born_date(correct_born_date(pesel1))}.')
            break
