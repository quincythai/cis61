def group_by(seq, fn): 
    """ 
    >>> group_by([12, 23, 14, 45], lambda p: p // 10) 
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(list(range(-3, 4)), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """
    d = {}

    for element in seq:
    	key = fn(element)

    	# if key doesn't exist yet, create the list
    	if key not in d:
    		d[key] = [element]
    	# else, key exists, so append
    	else:
    		d[key].append(element)

    return {k: d[k] for k in sorted(d)} 
