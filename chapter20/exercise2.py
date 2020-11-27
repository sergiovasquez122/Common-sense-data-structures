'''
2. You're writing a function that accepts an array of distinct integers from 0,
1, 2, 3, ... up to N. However, the array will be missing one integer, and your
function is to return the missing one.

For example, this array has all the integers from 0 to 6, but is missing the 4:

[2, 3, 0, 6, 1, 5]
'''
def find_missing_number(A):
    n = len(A)
    gauss_sum = ((n) * (n + 1)) / 2
    for e in A:
        gauss_sum -= e
    return gauss_sum
