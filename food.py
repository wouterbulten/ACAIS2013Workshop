import breve

class SimpleFood (breve.Mobile):

	def __init__(self):
		breve.Mobile.__init__(self)

		self.randomizedLocation()

	def iterate(self):
		None

	def randomizedLocation(self):

		randomLoc = breve.randomExpression(2 * breve.vector(10,0,10)) - breve.vector(10,0,10)

		self.move(randomLoc)