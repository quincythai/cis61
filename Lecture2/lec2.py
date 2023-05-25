def abs_val(x):
	if x > 0:
		return x
	elif x < 0:
		return -x
	else:
		return 0

def abs_val2(x):
	if x >= 0:
		return x
	else:
		return -x

def abs_val3(x):
	if x >= 0:
		return x
	return -x


def f(x):
	if x < 0:
		print("Below 0")
	elif x % 2 == 0:
		return "Even number"
	elif x % 3 == 0:
		return "Divisible by 3"


def fib(n):
	prev, curr = 0, 1
	k = 0
	while k < n:
		prev, curr = curr, prev + curr
		k += 1
	return prev




