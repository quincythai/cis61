def flatten(lst):
    """Returns a flattened version of lst.
    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    """
    
    # Base: if the list does not contain any lists inside, return lst. (normal list)
    if not any(type(elem) == list for elem in lst):
        return lst

    # Recursion: check if element is type list, and call flatten(elem) in order to turn it into a list
    result = []
    for elem in lst:
        if type(elem) == list:
            result += flatten(elem)
        else: # element is not type list
            result += [elem] # string concatenation with lists to combine them

    return result
