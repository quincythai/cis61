class Link:
	empty = () # empty tuple
	def __init__(self, first, rest=empty): # default is empty tuple
		assert rest is Link.empty or isinstance(rest, Link)
		# so either its empty or it points to another LinkedList type
		self.first = first
		self.rest = rest

def sum_link(lnk):
	"""Return sum of all elements in LinkedList"""

	# can also use "==" in place of "is"

	# Case: LinkedList is empty
	if lnk is Link.empty:
		return 0
	return lnk.first + sum_link(lnk.rest)

# Old function does not have case for empty linkedlist
def sum_link2(lnk):
	if link.rest is Link.empty:
		return lnk.first
	else:
		return lnk.first + sum_link(lnk.rest)

def display_link(lnk):
	"""Return a string of elements from linkedlist lnk"""

	string = "< "

	# as long as lnk (itself) is not empty
	while lnk is not Link.empty:
		# if the val element is a LinkedList
		if isinstance(lnk.first, Link):
			# recursively call function to make list within list
			elem = display_link(lnk.first)
		else:
			elem = str(lnk.first)
		string += elem + " "

		lnk = lnk.rest # go to next 

	return string + ">"

def display_link2(lnk):
	"""Return a string of elements from linkedlist lnk"""

	string = "< "

	# as long as lnk (itself) is not empty
	while lnk is not Link.empty:
		string += str(lnk.first) + " "
		lnk = lnk.rest # go to next

	string += ">"
	return string



def double_link(lnk):
	"""Return a NEW LinkedList with vals doubled"""

	if lnk is Link.empty:
		return Link.empty
	else:
		return Link(lnk.first * 2, double_link(lnk.rest))

def map_link(f, lnk):
	if lnk is Link.empty:
		return Link.empty

	else:
		return Link(f(lnk.first), map_link(f, lnk.rest))

def map_link_mute(f, lnk):
	if lnk is Link.empty:
		return

	# Mutate the value
	lnk.first = f(lnk.first)
	
	# Recursively call function
	map_link_mute(f, lnk.rest)

	# Note doesn't return anything





