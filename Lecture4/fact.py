def fact(n):
	"""
	>>> fact(0)
	1
	>>> fact(1)
	1
	>>> fact(3)
	6
	>>> fact(5)
	120
	"""
	if n == 0:
		return 1
	else:
		return n * fact(n-1)