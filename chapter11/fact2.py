def fact(n, i=1, product=1):
    return product if i > n else fact(n, i + 1, product * i)
