''' 
4. Use recursion to write a function that accepts a string and returns the
first index that contains the character “x.” For example, the string,
"abcdefghijklmnopqrstuvwxyz" has an “x” at index 23. To keep things simple,
assume the string definitely has at least one “x.”
'''
def find_first_idx_of_x(l, idx=0):
    if l[idx] == 'x': return idx
    return find_first_idx_of_x(l, idx+1)
