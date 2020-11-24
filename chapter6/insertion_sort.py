# comparisons 
# (N - 1) + (N - 2) + ... + 1 = ((N - 1) * N) / 2
# shifts
# (N - 1) + (N - 2) + ... + 1 = ((N - 1) * N) / 2
# removal
# (N - 1)
# insertion
# (N - 1)
# total
# O(N**2)
def insertion_sort(array):
    for index in range(1, len(array)):
        temp_value = array[index]
        position = index - 1
        while position >= 0:
            if array[position] > temp_value:
                    array[position + 1] = array[position]
                    position = position - 1

            else:
                 break

    return array
