def sorting_algos(arr):
    """selection sort algoritm"""
    if len(arr) < 2:
        return arr
    for cell in range(0, len(arr)):
        for item in range(cell+1, len(arr)):
            if arr[item] < arr[cell]:
                arr[item], arr[cell] = arr[cell], arr[item]

    return arr
