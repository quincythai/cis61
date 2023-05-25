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

def map_tree(f, t):
	#Mutate the value
	t.label = f(t.label)

	for b in t.branches:
		map_tree(f, b)


def prune(t, x):
    """
    >>> t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0)])])])
    >>> prune(t, 1)
    >>> t
    >>> Tree(3, [Tree(2)])
    """
    #optional
    if t.is_leaf():
        return
    t.branches = [b for b in t.branches if b.label != x]
    
    for b in t.branches:
        prune(b, x)



def prune2(t, x):
	"""
    >>> t = Tree(3, [Tree(1, [Tree(0), Tree(1)]), Tree(2, [Tree(1), Tree(1, [Tree(0)])])])
    >>> prune(t, 1)
    >>> t
    >>> Tree(3, [Tree(2)])
    """

    # If leaf, don't print anything
    if t.is_leaf():
    	return


    # Create a new tree
    # For each branch, see if label is x
    # If not x, include
    # If is x, do not include
    t.branches = [b for b in t.branches if b.label != x]

    # For remaining branches not x, call prune on them
    for b in t.branches:
    	prune(b, x)