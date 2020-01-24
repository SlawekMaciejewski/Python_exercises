from typing import List


def add_emp(emp: str, emp_list: List[str]=[]) -> List: # Pycharm podpowiada aby zamienic pustą listę na None
    emp_list.append(emp)
    return emp_list

def add_emp_ok(emp: str, emp_list: List[str]=None) -> List:
    if not emp_list:
        emp_list = []
    emp_list.append(emp)
    return emp_list


if __name__ == '__main__':
    emps = ['Ania', 'Jarek']
    print(add_emp('Tomek', emps[:])) # płytka kopia aby nie nadpisać listy emps, bo będzie 2xTomek
    print(add_emp('Darek'))
    print(add_emp('Robert'))
    print(emps)

    print('**********************')

    print(add_emp_ok('Tomek', emps))
    print(add_emp_ok('Darek'))
    print(add_emp_ok('Robert'))
    print(emps) # bez płytkiej kopii nadpisujemy listę emps i mamy [Ania, Jarek, Tomek]