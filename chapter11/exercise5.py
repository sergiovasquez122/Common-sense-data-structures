'''
5. This problem is known as the “Unique Paths” problem: Let’s say you have
a grid of rows and columns. Write a function that accepts a number of rows
and a number of columns, and calculates the number of possible “shortest”
paths from the upper-leftmost square to the lower-rightmost square.
'''
def unique_paths(m, n):
    if m < 0 or n < 0: return 0
    if m == 0 and n == 0: return 1
    return unique_paths(m - 1, n) + unique_paths(m, n - 1)
