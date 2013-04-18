import breve

class SimpleAgent (breve.Mobile):

	def __init__(self):
		breve.Mobile.__init__(self)

		print "Created agent"

	def iterate(self):
		None


class RandomAgent (breve.Wanderer):
	def __init__(self):
		breve.Wanderer.__init__(self)

		self.setWanderRange(breve.vector(10, 0, 10))
		print "Created agent"

	def iterate(self):
		breve.Wanderer.iterate(self)