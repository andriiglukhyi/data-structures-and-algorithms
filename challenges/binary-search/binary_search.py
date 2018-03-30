def sub_binary_search(arr, val, low, high):
    if low > high:
        return False
    elif len(arr) == 1 and arr[0] is not val:
        return False
    else:
        mid = (low+high)//2
        if val == arr[mid]:
            print(arr[mid])
            return mid
        elif val < arr[mid]:
            return sub_binary_search(arr, val, low, mid-1)
        else:
            return sub_binary_search(arr, val, mid+1, high)


def binary_search(arr, val):
    if len(arr) == 0:
        return False
    elif type(val) != int:
        return False
    else:
        low = 0
        high = len(arr)
        sub_binary_search(arr, val, low, high)
        return False