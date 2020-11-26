'''

Here is a solution to the “Unique Paths” problem from an exercise in the
previous chapter. Use memoization to improve its efficiency:e
'''
def unique_paths(rows, columns):
    if rows == 1 or columns == 1:
        return 1
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)

def unique_paths_better(rows, columns, memo={}):
    if rows == 1 or columns == 1:
        return 1
    if (rows, columns) not in memo:
        memo[(rows, columns)] = unique_paths_better(rows - 1, columns) + unique_paths_better(rows, columns - 1)
    return memo[(rows, columns)]
