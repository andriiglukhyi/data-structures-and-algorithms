def find_brute(S, P):
    """
    Return the lovest index of S at which substring P begins 
    """
    n, m = len(S), len(P)
    for i in range(n-m+1):
        k == 0
        while k < m and S[i+k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1
