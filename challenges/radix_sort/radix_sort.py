def radix_sort(array):
    if len(array) < 2:
        return array
    maxLen = int(len(str(max(array))))
    buckets = [[] for i in range(0, 10)]
    for digit in range(0, maxLen):
        for number in array:
            buckets[int(number / 10**digit % 10)].append(number)
        del array[:]
        for bucket in buckets:
            array.extend(bucket)
            del bucket[:]
    return array