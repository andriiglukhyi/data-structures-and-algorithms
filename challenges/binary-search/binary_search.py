def sub_binnarySearch(arr, val, low, high):
    if low>high:
        False
    else:
        mid = (low+high)//2
        if val == arr[mid]:
            print(mid)
            return mid
        elif val<arr[mid]:
            return sub_binnarySearch(arr,val,low, mid-1)
        else:
            return sub_binnarySearch(arr,val,mid+1, high)
def binnarySearch(arr,val):

    if len(arr) == 0:
        return -1
    elif type(val) != int:
        return -1
    elif val not in arr:
        return -1
    else:
        low = 0
        high = len(arr)
        sub_binnarySearch(arr, val, low, high)
    
    
if __name__ == '__main__':
    binnarySearch(range(300,400), 350)