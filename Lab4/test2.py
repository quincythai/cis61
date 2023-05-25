def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    def hailstone_helper(n, count):
        if n == 1:
            print(n)
            return count

        print(n)
        if n % 2 == 0:
            return hailstone_helper(n//2, count+1)
        else:
            return hailstone_helper(3*n+1, count+1)

    return hailstone_helper(n, 1)