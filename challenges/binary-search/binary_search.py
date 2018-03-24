def sub_binary_search(arr, val, low, high):
    if low>high:
        False
    else:
        mid = (low+high)//2
        if val == arr[mid]:
            print (arr[mid])
            return mid
        elif val<arr[mid]:
            return sub_binary_search(arr,val,low, mid-1)
        else:
            return sub_binary_search(arr,val,mid+1, high)
    return False
    
def binary_search(arr,val):

    if len(arr) == 0:
        return -1
    elif type(val) != int:
        return -1
    else:
        low = 0
        high = len(arr)
        sub_binary_search(arr, val, low, high)
    
    
if __name__ == '__main__':
    binary_search([1,2,3,4,11,6,7], 11)