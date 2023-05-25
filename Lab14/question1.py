def naturals():
    """Yield an infinite sequence of natural numbers, starting from 1."""
    n = 1
    while True:
        yield n
        n += 1


# Yield doesn't actually mutate values, it returns iterator to new value
# Function becomes generator function when you use keyword yield
# Yield from - yields all values from an iterable
# and also results of another generator functioon


def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """

    # bookmark = iter(s) # s is a list
    # while True:
    #     try:
    #         x = next(bookmark) # returns current elem, then moves bookmark to next elem
    #         yield x * k
    #     except StopIteration: # if at end of list, then error.
    #         return

    yield from (num * k for num in s)
