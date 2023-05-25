def merge(lst1, lst2):
    """Merges two sorted lists.
    >>> merge([1], [2])
    [1, 2]
    >>> merge([2], [1])
    [1, 2]
    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    if not lst1 or not lst2:
        return []
    elif lst1[0] < lst2[0]:
        return [lst1[0]] + merge(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge(lst1, lst2[1:])''