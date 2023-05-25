def add_chars(w1, w2):
    """
    Return a string containing the characters you need to add to w1 to get w2.
    You may assume that w1 is a subsequence of w2.

    >>> add_chars("owl", "howl")
    'h'
    >>> add_chars("want", "wanton")
    'on'
    >>> add_chars("rat", "radiate")
    'diae'
    >>> add_chars("a", "prepare")
    'prepre'
    >>> add_chars("resin", "recursion")
    'curo'
    >>> add_chars("fin", "effusion")
    'efuso'
    >>> add_chars("coy", "cacophony")
    'acphon'
    """

    # Base: if subsequence w1 is empty, add remainder of w2.
    if w1 == "":
        return w2

    else: # Recursion: adding leftmost char based on case, and then calling method with next letter.
    	if w1[0] == w2[0]: # if 1st chars match, call function with the next letters for both
    		return add_chars(w1[1:], w2[1:])
    	else:	# first chars don't match, so add leftmost w2 char, and then continue traversing w2.
        	return w2[0] + add_chars(w1, w2[1:])