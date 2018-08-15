def compute_kmp_fail(P):
    """
    Utility that computes and returns KMP fail list.
    """
    m = len(P)
    # by default presume overlap 0 everyvhere
    fail = [0 for x in range(m)]
    j = 1
    k = 0
    while j < m:
        if P[j] == P[k]:
            fail[j] = k+1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k-1]
        else:
            j += 1
    return fail
    
def find_kmp(T, P):
    """
    Return the lowest index of T at which substring P begins (or else -1).
    """
    # more convenient notation
    n, m = len(T), len(P)
    if m == 0:
        return 0
        fail = compute_kmp_fail(P)
    j = 0
    k = 0
    while j < n:
        if T[j] == P[k]:
            if k == m-1:
                return j - m + 1
            j += 1 # try to extend match
            k += 1
            elif k > 0:
                k = fail[k−1] # reuse suffix of P[0:k]
            else:
                j += 1
    return -1
