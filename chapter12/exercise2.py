'''
2. The following function uses recursion to calculate the Nth number from
a mathematical sequence known as the “Golomb sequence.” It’s terribly
inefficient, though! Use memoization to optimize it. (You don’t have to
actually understand how the Golomb sequence works to do this exercise.)
'''
def golomb(n):
    if n == 1:
        return 1
    return 1 + golomb(n - golomb(golomb(n - 1)))

def golomb_better(n, memo={}):
    if n == 1:
        return 1
    if n not in memo:
        memo[n] = 1 + golomb_better(n - golomb_better(golomb_better(n - 1)))
    return memo[n]
