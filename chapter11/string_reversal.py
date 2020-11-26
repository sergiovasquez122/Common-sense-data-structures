def reverse(s, idx=0):
    return "" if idx >= len(s) else reverse(s, idx + 1) + s[idx]
