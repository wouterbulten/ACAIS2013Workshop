import breve

class SimpleFood (breve.Mobile):

	def __init__(self):
		breve.Mobile.__init__(self)

		self.randomizedLocation()

		# Owner of this food source
		self.owner = None

		# A nice red color
		self.setColor(breve.vector(255,0,0))

		# Set the shape of the food source
		cube = breve.createInstances(breve.Sphere, 1).initWith(0.5)
		self.setShape(cube)

	def iterate(self):
		None

	def randomizedLocation(self):

		randomLoc = breve.randomExpression(2 * breve.vector(20,0,20)) - breve.vector(20,0,20)

		self.move(randomLoc)

	def setOwner(self, o):
		self.owner = o

	def getOwner(self):
		return self.owner
