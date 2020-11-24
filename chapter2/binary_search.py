def binary_search(arr, search_value):
    low = 0
    hi = len(arr) - 1
    while low <= hi:
        mid = (low + hi) // 2
        if arr[mid] < search_value:
            low = mid + 1
        elif arr[mid] > search_value:
            hi = mid + 1
        else:
            return mid
    return None
