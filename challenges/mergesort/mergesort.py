def mergesort(arr):
    """merge sort function which takes arr as an argument"""
    # check if array already sorted
    def move(s1, s2, arr):
        """merge subarray"""
        arr = [0]*(len(s1)+len(s2))
        i = j = 0
        while i+j < len(arr):
            if j == len(s2) or i < len(s1) and s1[i] < s2[j]:
                arr[i+j] = s1[i]
                i += 1
            else:
                arr[i+j] = s2[j]
                j += 1
        return arr
    if len(arr) < 2:
        return arr
    temp = []
    midle = len(arr)//2
    s1 = arr[:midle]
    s2 = arr[midle:]
    a = mergesort(s1)
    b = mergesort(s2)
    end = move(a, b, temp)
    return end
