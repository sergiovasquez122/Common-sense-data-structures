'''
Use recursion to write a function that accepts an array of strings and
returns the total number of characters across all the strings. For example,
if the input array is ["ab", "c", "def", "ghij"] , the output should be 10
since there
are 10 characters in total.
'''
def total_characters(l, idx=0):
    if idx >= len(l):
        return 0
    return len(l[idx]) + total_characters(l, idx + 1)
