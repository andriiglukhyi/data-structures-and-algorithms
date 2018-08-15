def find_boyer_moore(T, P):
    """
    Return the lowest index of T at which substring P begins or else -1 
    """
    # introduce convenient notation
    n, m = len(T), len(P)
    if m == 0:
        return 0
    if n == 0:
        return False
    # build dict
    last = {}
    # go thru the pattern and add it to the dict
    for k in range(m):
        last[P[k]] = k
    # align end of pattern at index m-1 of text
    k = i = m - 1
    while i < n:
        if T[i] == P[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(T[i], -1])
            i += m - min(k, j + 1)
            k = m-1
    return -1
    
    