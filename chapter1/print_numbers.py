def print_numbers_version_one():
    number = 2

    while number <= 100:
        if number % 2 == 0:
            print(number)
        number += 1

def print_number_version_two():
    number = 2
    while number <= 100:
        print(number)
        number += 2

'''Which of these functions is faster?

function two requires half as many operations
as function 1
'''
