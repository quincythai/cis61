def enumerate(s, start=0):
    """Returns a list of lists, where the i-th list contains i+start and
    the i-th element of s.
    >>> enumerate([6, 1, 'a']) # len(s) = 3
    [[0, 6], [1, 1], [2, 'a']]
    >>> enumerate('five', 5)
    [[5, 'f'], [6, 'i'], [7, 'v'], [8, 'e']]
    """
    return [[start, s[0]]] + [[i+start, s[i]]for i in range(1, len(s))] 

    #range(1, len(s)) = range(1, 3) = (1, 2)
