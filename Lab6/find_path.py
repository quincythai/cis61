from tree import *

def find_path(tree, x): 
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)]) 
    >>> find_path(t, 5) 
    [2, 7, 6, 5]
    >>> find_path(t, 10)
    """ 
    if label(tree) == x:
        return tree
    else:
        for b in branches(tree):
            path = find_path(b, x)
            if path:
                return [label(tree)] + path

    return None
