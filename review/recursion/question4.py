def count_stair_ways(n):
    """
    >>> count_stair_ways(1)
    1
    >>> count_stair_ways(2)
    2
    >>> count_stair_ways(3)
    3
    >>> count_stair_ways(4)
    5
    """
    if n == 1 or n == 0:
        return 1
    else:
        return count_stair_ways(n-1) + count_stair_ways(n-2)