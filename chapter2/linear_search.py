def linear_search(arr, search_value):
    for i in range(len(arr)):
        if arr[i] == search_value:
            return i
        elif arr[i] > search_value:
            break
    return None
