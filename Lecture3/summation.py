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
	return summation(n, identity)
	

def sum_cubes(n):
	"""Sum the first N cubes
	>>> sum_cubes(5)
	225
	"""
	return summation(n, cube)

def identity(x):
	return x

def cube(x):
	return pow(x, 3)
	

def square(x):
	return pow(x, 2)

def sum_squares(n):
	"""Sum the first N squares
	>>> sum_squares(5)
	225
	"""
	return summation(n, square)
