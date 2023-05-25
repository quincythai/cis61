class Animal:
	legs = 0

	def __init__(self, name, owner):
		self.name = name
		self.owner = owner

class Dog(Animal):
	legs = 4

	# inherit Animal's init

	def speak(self):
		print("Woof!")

	def fetch(self, item):
		print("I fetched " + str(item))

class Chicken(Animal):
	legs = 4

	# inherit init

	def speak(self):
		print("Cluck!")

class GoldenRetriever(Dog):
	# inherit legs

	# inherit init

	breed = 'Golden Retriever'