def array_sum(a, idx=0):
    return 0 if idx >= len(a) else a[idx] + array_sum(a,idx + 1)
