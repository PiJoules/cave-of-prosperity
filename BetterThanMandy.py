from copy import deepcopy

class BetterThanMandy(object):
	def __init__(self, limit, nuggets):
		self.limit = limit
		self.nuggets = nuggets
		self.maximize_profits()

	def maximize_profits(self):
		limit = self.limit
		nuggets = self.nuggets
		count = len(nuggets)

		nuggets = sorted(nuggets, reverse=True)
		
		all_sums = self.possible_sums(nuggets, limit)
		self.total = 0
		self.chosen_nuggets = []
		for s, dese_nuggets in all_sums:
			if s > self.total:
				self.total = s
				self.chosen_nuggets = dese_nuggets

	"""
	Return an array containing all possible sums of the given array of nuggets
	along with their corresponding nuggets.
	"""
	def possible_sums(self, nuggets, limit):
		nugget = nuggets[0]
		if len(nuggets) <= 1:
			if nugget <= limit:
				return [ (0, []), (nugget, [nugget]) ]
			else:
				return [ (0, []) ]

		sums = self.possible_sums(nuggets[1:], limit)
		next_sums = []
		for s, dese_nuggets in sums:
			if s + nugget < limit:
				next_sums.append( (s+nugget, deepcopy(dese_nuggets) + [nugget]) )
		return sums + next_sums

	def print_backpack_weight(self):
		print self.total

	def print_nuggets(self):
		for nugget in self.chosen_nuggets:
			print nugget