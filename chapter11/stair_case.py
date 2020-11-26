def ways_to_top(n):
    if n < 0:
        return 0
    if n in [0, 1]:
        return 1
    return ways_to_top(n - 1) + ways_to_top(n - 2) + ways_to_top(n - 3)
