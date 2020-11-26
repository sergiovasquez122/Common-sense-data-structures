def double_array(arr, idx=0):
    if idx == len(arr):
        return
    arr[idx] *= 2
    double_array(arr, idx + 1)
