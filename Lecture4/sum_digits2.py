def sum_digits(n):
	"""Calculates the sum of the digits n
	>>> sum_digits(9)
	9
	>>> sum_digits(10)
	1
	>>> sum_digits(2019)
	12
	"""
	if n < 9:
		return n
	else:
		return n % 10 + sum_digits(n // 10)

def sum_digits2(n):
	if n < 10:
		return n
	else:
		last_digit = n % 10
		all_except_last = n // 10
		return last_digit + sum_digits2(all_except_last)