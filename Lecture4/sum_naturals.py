def nats(n):
	"""
	>>> nats(2)
	3
	>>> nats(3)
	6
	>>> nats(5)
	15
	"""
	if n == 0:
		return 0
	else:
		return n + nats(n-1)