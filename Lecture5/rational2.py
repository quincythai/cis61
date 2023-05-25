from math import gcd
def rational(n, d):
	"""A representation of the rational number"""
	gcd_a_b = gcd(n, d)
	return {"numer": n // gcd_a_b, "denom": d // gcd_a_b}

def numer(x):
	"""Return the numberator of rational number"""
	return x["numer"]

def denom(x):
	"""Return denom of rational num"""
	return x["denom"]

########################################

#implementation
def mul_rational(x, y):
	"""Sum of rational numbers X and Y"""
	nx = numer(x)
	ny = numer(y)
	dx = denom(x)
	dy = denom(y)
	return rational(nx*ny, dx*dy)

def add_rational(x, y):
	"""Sum of rational numbers X and Y"""
	nx = numer(x)
	ny = numer(y)
	dx = denom(x)
	dy = denom(y)
	return rational(nx*dy + ny*dx, dx*dy)

def print_rational(x):
	"""Print rational X"""
	print(numer(x), "/", denom(x))

def rationals_are_equal(x, y):
	"""True if rational nums X and Y are equal"""
	return numer(x) * denom(y) == numer(y) * denom(x)
