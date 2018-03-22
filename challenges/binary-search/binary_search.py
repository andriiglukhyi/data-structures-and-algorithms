def sub_binary_search(arr, val, low, high):
    if low>high:
        False
    else:
        mid = (low+high)//2
        if val == arr[mid]:
            print(mid)
            return mid
        elif val<arr[mid]:
            return sub_binary_search(arr,val,low, mid-1)
        else:
            return sub_binary_search(arr,val,mid+1, high)
def binary_search(arr,val):

    if len(arr) == 0:
        return -1
    elif type(val) != int:
        return -1
    elif val not in arr:
        return -1
    else:
        low = 0
        high = len(arr)
        sub_binary_search(arr, val, low, high)
    
    
if __name__ == '__main__':
    binary_search(range(300,400), 350)