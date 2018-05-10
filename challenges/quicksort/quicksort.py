def quicksort(arr):
    """quick sort function"""
    if len(arr) < 2:
        return
    quicksort2(arr, 0, len(arr)-1)
    return arr


def quicksort2(a, low, hi):
    """check if there any item should be sorted"""
    # import pdb; pdb.set_trace()
    if low < hi:
        pivot = partition(a, low, hi)
        quicksort2(a, low, pivot - 1)
        quicksort2(a, pivot + 1, hi)


def get_pivot(a, low, hi):
    """find optimal pivot"""
    mid = (hi+low)//2
    if a[low] < a[mid]:
        if a[mid] < a[hi]:
            pivot = mid
    elif a[low] < a[hi]:
        pivot = low
    pivot = hi
    return pivot


def partition(a, low, hi):
    """make partition for recursive calls"""
    pivotindex = get_pivot(a, low, hi)
    pivot_val = a[pivotindex]
    a[pivotindex], a[low] = a[low], a[pivotindex]
    border = low
    for i in range(low, hi + 1):
        if a[i] < pivot_val:
            border += 1
            a[i], a[border] = a[border], a[i]
    a[low], a[border] = a[border], a[low] 
    return pivotindex


