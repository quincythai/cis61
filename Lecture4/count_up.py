def count_up(n):
	"""Prints the numbers from 1 to n.
	>>> count_up(1)
	1
	>>> count_up(2)
	1
	2
	>>> count_up(4)
	1
	2
	3
	4
	"""
	if n == 1:
		print(1)
	else:
		count_up(n-1)
		print(n)

def count_up2(n):
	if n > 1: # base case not explicitly defined
		count_up(n-1)
	print(n)