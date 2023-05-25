#Generator
def naturals():
	"""
	>>> nats = naturals()
	>>> next(nats)
	0
	>>> next(nats)
	1
	>>> next(nats)
	2
	"""
	x = 0
	while True:
		yield x
		x += 1