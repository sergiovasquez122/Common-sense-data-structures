def fib(n, memo={}):
    if n == 0 or n == 1:
        return 1
    if n not in memo:
        memo[n] = fib(n - 1) + fib(n - 2)
    return memo[n]
