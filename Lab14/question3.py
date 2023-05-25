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


def cumulative_sum(t):
    """Mutates t so that each node's label becomes the sum of 
       all labels in the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """

    # Cannot use total variable without modifying parameter list

    # Base: if leaf, simply return the tree for the recursive part
    if t.is_leaf():
    	return t # return the tree itself

    else:
    	for b in t.branches:
    		cumulative_sum(b) # recursive call on the subtree
    		t.label += b.label # get subtree's value and add it to current

    # No need to return, because we are mutating