def couple(s1, s2):
    """Return a list that contains lists with i-th elements of two sequences
    coupled together.
    >>> s1 = [1, 2, 3]
    >>> s2 = [4, 5, 6]
    >>> couple(s1, s2)
    [[1, 4], [2, 5], [3, 6]]
    >>> s3 = ['c', 6]
    >>> s4 = ['s', '1']
    >>> couple(s3, s4)
    [['c', 's'], [6, '1']]
    """
    assert len(s1) == len(s2), "Lengths must be the same."

    return [[s1[i], s2[i]] for i in range(len(s1))]
    # len s1 = 3
    # range(3) = (0, 1, 2)
    # return [ s1[i], s2[i] for i in (0, 1, 2)]