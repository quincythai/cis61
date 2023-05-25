from tree import *

def sprout_leaves(t, vals):
    """Sprout new leaves containing the data in vals at each leaf in
    the original tree t and return the resulting tree.
    >>> t1 = tree(1, [tree(2), tree(3)])
    >>> print_tree(t1)
    1
      2
      3
    >>> new1 = sprout_leaves(t1, [4, 5])
    >>> print_tree(new1)
    1
      2
        4
        5
      3
        4
        5
    >>> t2 = tree(1, [tree(2, [tree(3)])])
    >>> print_tree(t2)
    1
      2
        3
    >>> new2 = sprout_leaves(t2, [6, 1, 2])
    >>> print_tree(new2)
    1
      2
        3
          6
          1
          2
    """
    if is_leaf(t): # make sure to return (#, [tree(#)]) format
      return tree(label(t), [tree(v) for v in vals]) 

    else:
      lst_trees = [] # make list to store returned sprouted trees
      for b in branches(t): 
        lst_trees += [sprout_leaves(b, vals)] #ensure concatenation with [result]

      return tree(label(t), lst_trees) # END: return root plus new sprouted branches


