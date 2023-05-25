from math import gcd

class Rational:

	def __init__(self, n, d):
		gcd_n_d = gcd(n, d)
		self.numer = n // gcd_n_d
		self.denom = d // gcd_n_d

	def getNumer(self):
		return self.numer

	def getDenom(self):
		return self.denom

	def mul_rational(self, other):
		return Rational(self.numer*other.numer, self.denom*other.denom)

	def print(self):
		print(self.numer, "/", self.denom)
