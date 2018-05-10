def radix_sort(lst):
    if len(lst) < 2:
        return lst
    max_number = len(str(max(lst)))
    lst = list(lst)

    for digit in range(max_number):
        flag = []
        buckets = [[]]*10
        for item in range(len(lst)):    
            if str(lst[item])[digit]:
                buckets[int(str(lst[item])[digit])].append(lst[item])
            else:
                buckets[0].append(lst[item])
            if lst[item +1]:
                if lst[item] < lst[item + 1]:
                    flag.append(1)
                else:
                    flag.append(0)
        if 0 in flag:
            lst = []
            for item in buckets:
                lst += item
        else:
            return lst
