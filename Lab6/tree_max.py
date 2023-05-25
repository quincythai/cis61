from tree import tree, label, branches, is_tree, is_leaf

def tree_max(t):
    """Return the maximum label in a tree.
    >>> t = tree(4, [tree(2, [tree(1)]), tree(10)])
    >>> tree_max(t)
    10
    """
    # Method checks left and right side of trees, returning the largest node in each.

    # Base case: if the tree is a leaf, return the label
    if is_leaf(t):
        return label(t)

    # Recursive case: find the maximum label in the branches of the tree
    max_label = label(t)
    for b in branches(t):
        branch_max = tree_max(b)
        if branch_max > max_label:
            max_label = branch_max

    return max_label

def tree_max2(t):
    """Return the maximum label in a tree."""
    # Base case: if the tree is a leaf, return the label
    if is_leaf(t):
        return label(t)

    # Recursive case: get the labels of all the nodes in the tree
    labels = [label(t)]
    for b in branches(t):
        labels += tree_max2(b)

    # Return the maximum label in the list
    return max(labels)
