class Link:
    empty = () # empty tuple
    def __init__(self, first, rest=empty): # default is empty tuple
        assert rest is Link.empty or isinstance(rest, Link)
        # so either its empty or it points to another LinkedList type
        self.first = first
        self.rest = rest

def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    # Iterative
    # lst = []

    # while link is not Link.empty:
    #     lst.append(link.first)
    #     link = link.rest

    # return lst

    # Recursive
    if link is Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)
