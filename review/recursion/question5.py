def count_k(n, k):
    """ 
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1 
    4
    >>> count_k(4, 4) 
    8 
    >>> count_k(10, 3) 
    274
    >>> count_k(300, 1)
    1 
    """
    if k == 1:
        return 1

