class Account:
	# class attribute
	max_withdrawal = 10

	# initializer (constructor)
	def __init__(self, holder):
		self.name = holder
		self.balance = 0

	def desposit(self, amount):
		self.balance += amount
		return self.balance

	def withdraw(self, amount):
		self.balance -= amount
		return self.balance

