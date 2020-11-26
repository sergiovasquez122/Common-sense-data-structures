'''
1. The following function accepts an array of numbers and returns the sum,
as long as a particular number doesn’t bring the sum above 100. If adding
a particular number will make the sum higher than 100, that number is
ignored. However, this function makes unnecessary recursive calls. Fix
the code to eliminate the unnecessary recursion:
wing function accepts an array of numbers and returns the sum,
as long as a particular number doesn’t bring the sum above 100. If adding
a particular number will make the sum higher than 100, that number is
ignored. However, this function makes unnecessary recursive calls. Fix
the code to eliminate the unnecessary recursion:
'''
def add_until_100(array):
    if len(array) == 0:
        return 0
    if array[0] + add_until_100(array[1:]) > 100:
        return add_until_100(array[1:])
    return array[0] + add_until_100(array[1:])

def add_until_100_better(array, idx=0):
    if idx >= len(array):
        return 0
    remainder = add_until_100_better(array, idx + 1)
    if array[idx] + remainder < 100:
        return array[idx] + remainder
    return remainder
