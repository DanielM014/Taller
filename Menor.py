def menor(arr):
    lowest = arr[0]
    for num in arr:
        if num < lowest:
            lowest = num
    return lowest