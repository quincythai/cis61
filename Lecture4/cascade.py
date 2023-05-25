def cascade(n):
	if n < 10: # if n single digit
		print(n)
	else:
		print(n)
		cascade(n // 10)
		print(n)
