'''
Write a function that returns the first non-duplicated character in a string.
For example, the string, "minimum" has two characters that only exist
once—the "n" and the "u" , so your function should return the "n" , since it
occurs first. The function should have an efficiency of O(N).
'''
def first_non_duplcate(A):
    l1 = {}
    for x in A:
        if x not in l1:
            l1[x] = 1
        else:
            l1[x] += 1
    for x in A:
        if l1[x] == 1:
            return x
    return None
