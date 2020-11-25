def print_lists(a):
    if isinstance(a, int):
        print(a)
        return
    for x in a:
        if isinstance(a, int):
            print(x)
        else:
            print_lists(x)
