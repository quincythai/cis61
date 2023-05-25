#Constructor
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] +  list(branches)
#Selectors
def label(tree):
    return tree[0]
def branches(tree):
    return tree[1:]
def is_tree(tree):
    if type(tree) == list and len(tree) > 0:
        return True
    else:
        return False
def is_leaf(tree):
    return not branches(tree)
    # Does node have any other nodes?
    # not branches(tree) returns True if empty; False if occupied



t1 = tree(3, [tree(1), tree(2, [tree(1), tree(1)])])
t2 = tree('A', [tree('B'), tree('C', [tree('D'), tree('E')])])
t3 = tree(8,
          [tree(4,
                [tree(2), tree(3)]),
           tree(3,
                [tree(1), tree(1,
                               [tree(1), tree(1)])])])

#Count Nodes
def count_nodes(t):
    if is_leaf(t): # base case
        return 1

    total = 0
    for b in branches(t): # recurisve call
        total += count_nodes(b)

    return 1 + total # 1 is for root

def count_nodes2(t):
    if is_leaf(t):
        return 1

    lst = [count_nodes2(b) for b in branches(t)]
    # [sum of left tree, sum of right tree]
    return sum(lst, 1)

def count_leaves(t):
    if is_leaf(t): # base case
        return 1

    total = 0
    for b in branches(t): # recurisve call
        total += count_nodes(b)

    return total

def count_leaves2(t):
    if is_leaf(t):
        return 1

    lst = [count_nodes2(b) for b in branches(t)]
    # [sum of left tree, sum of right tree]
    return sum(lst)

def collect_leaves(t):
    if is_leaf(t):
        return str(label(t))

    lst = []
    for b in branches(t): # call collect_leaves on each branch
        lst += collect_leaves(b)

    return "".join(lst)

def print_tree(t, indent=0):
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def square_tree(t):
    if is_leaf(t):
        return tree(label(t) * 2)

    lst = []
    for b in branches(t):
        lst += [square_tree(b)] # have to make it a list in order to concatenate

    new_label = tree(label(t) * 2)

    return tree(new_label, lst)









