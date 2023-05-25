def count_k(n, k):
    """ 
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1 
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3) 
    274
    >>> count_k(300, 1) # Only one step at a time 
    1
    """
    if n == 0: # successfully made it to the top
        return 1
    elif n < 0: # over stepped
        return 0
    else:
        # count_k(n-1, k) + count_k(n-2) + ... + count_k(n-k, k)
        total = 0
        i = 1
        while i <= k:
            total += count_k(n-i, k)
            i += 1
        return total
