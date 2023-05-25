from tree import *

def prune_leaves(t, vals):
    """Return a modified copy of t with all leaves that have a label that appears 
    in vals removed.  Return None if the entire tree is pruned away.
    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6,[tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
      2
      3
        5
      6
    """
    if is_leaf(t): # if leaf Node
        if label(t) in vals: # if leaf's value is in list to be removed
            return None # cut leaf
        else: # otherwise, return the Node
            return t 

    else:
        initial = []
        for b in branches(t):
            intial += [prune_leaves(b, vals)]

        trimmed = []
        for b in trimmed:
            if b is not None:
                trimmed += [b]

        return tree(label(t), trimmed)


