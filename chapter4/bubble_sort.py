def bubble_sort(l):
    unsorted_until_index = len(l) - 1
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(unsorted_until_index):
            if l[i] > l[i + 1]:
                l[i], l[i + 1] = l[i + 1], l[i]
                is_sorted = False
        unsorted_until_index -= 1
    return l

print(bubble_sort([65, 55, 45, 35, 25, 15, 10]))
