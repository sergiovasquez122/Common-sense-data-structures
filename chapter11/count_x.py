def count_x(s, idx=0):
    if idx >= len(s):
        return 0
    value = 0 if s[idx] != 'x' else 1
    return value + count_x(s, idx + 1)
