def compute_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        resulte = 'underweight'
    elif bmi > 25:
        resulte = 'overweight'
    else:
        resulte = ' normal'
    return resulte


if __name__ == '__main__':
    my_weight = float(input('Your weight [kg]: '))
    my_height = float(input('Your height [m]: '))
    print(compute_bmi(my_weight, my_height).capitalize())
