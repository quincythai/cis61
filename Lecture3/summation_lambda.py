from math import pi, sqrt

def summation(n, term):
	total = 0
	k = 0

	while k <= n:
		total = total + term(k)
		k = k + 1
	return total

def sum_naturals(n):
	""" Sum the first N natural numbers
	>>> sum_naturals(5)
	15
	"""
	return summation(n, lambda x: x)

def sum_squares(n):
	"""Sum the first N squares
	>>> sum_squares(5)
	225
	"""
	return summation(n, lambda x: x * x) 

def sum_cubes(n):
	"""Sum the first N cubes
	>>> sum_cubes(5)
	225
	"""
	return summation(n, lambda x: x * x * x)