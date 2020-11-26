'''
2. The following function finds the “missing number” from an array of inte-
gers. That is, the array is expected to have all integers from 0 up to the
array’s length, but one is missing. As examples, the array, [5, 2, 4, 1, 0] is
missing the number 3, and the array, [9, 3, 2, 5, 6, 7, 1, 0, 4] is missing the
number 8.
'''
def find_missing_number(array):
    for i in range(len(array)):
        if i not in array:
            return i
    return None

def find_missing_number_better(array):
    b = array[:]
    b.sort()
    for i in range(len(b)):
        if b[i] != i:
            return i
    return None

