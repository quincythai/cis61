class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches

    def is_leaf(self):
        return not self.branches

def print_tree(t, indent=0):

    # 0 will print no spaces
    print(" " * indent + str(t.label))
    for b in t.branches:
        print_tree(b, indent+1)


def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.
    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    True
    """

    if t.is_leaf():
        return True
    if len(t.branches) == 1:
        return True
    if len(t.branches) > 2:
        return False
    if len(t.branches) == 2:
        if t.branches[0].label > t.label and t.branches[1].label <= t.label:
            return False
    for b in t.branches:
        return is_bst(b)
