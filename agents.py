import food
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

		# Set the shape of the agent
		cube = breve.createInstances(breve.Cube, 1).initWith(breve.vector(1,1,1))
		self.setShape(cube)

		# Set initial position to random
		self.randomizeLocation()

		# Setup the collision
		self.handleCollisions('SimpleFood', 'collisionWithFood')

		# Store a possible food source
		self.carrying = None

		print "Created agent"

	def iterate(self):
		breve.Wanderer.iterate(self)


	def collisionWithFood(self, f):
		
		if(f.getOwner()):
			return

		if(self.carrying != None):
			self.placeFoodObject(self.carrying, f)
			self.carrying = None
			return

		self.carrying = f
		self.carrying.setOwner(self)

	def placeFoodObject(self, ownFood, placedFood):

		location = placedFood.getLocation()
		location = location + ( breve.randomExpression( breve.vector( 2, 0, 2 ) ) - breve.vector( 1, 0, 1 ) )

		ownFood.move(location)
		ownFood.setOwner(0)

