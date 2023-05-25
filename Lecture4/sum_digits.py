def sum_digits(n):
	"""Calculates the sum of the digits n
	>>> sum_digits(9)
	9
	>>> sum_digits(10)
	1
	>>> sum_digits(2019)
	12
	"""
	if n//10 == 0:
		return n
	else:
		return n % 10 + sum_digits(n//10)

