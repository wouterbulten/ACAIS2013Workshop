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

		self.setWanderRange(breve.vector(20.0, 0.0, 20.0))

		# Set the shape of the agent
		cube = breve.createInstances(breve.Cube, 1).initWith(breve.vector(1,1,1))
		self.setShape(cube)

		# Set initial position to random
		self.randomizeLocation()

		# Setup the collision
		self.handleCollisions('SimpleFood', 'collisionWithFood')

		# Store a possible food source
		self.carrying = None

		# Group number of this agent
		self.group = 0

		# Timer to prevent to inhibit the collision behavior
		self.collidedTimer = 0

		print "Created agent"

	def iterate(self):
		# Update our food object
		if(self.carrying):
			self.carrying.move( ( self.getLocation() - breve.vector( 1, 0, 0 ) ) )

		self.collidedTimer -= 1

		breve.Wanderer.iterate(self)

	def collisionWithFood(self, f):
		
		if(f.getOwner()):
			return

		# We want two iterations without an collision
		if(self.collidedTimer > 0):
			self.collidedTimer = 2

		# Set the timer for the collision
		self.collidedTimer = 2

		if(self.carrying != None and self.carrying.getGroup() == f.getGroup()):
			self.placeFoodObject(self.carrying, f)
			self.carrying = None
			return

		self.carrying = f
		self.carrying.setOwner(self)
		self.carrying.setColor(self.getColor())
		self.carrying.setGroup(self.group)

	def placeFoodObject(self, ownFood, placedFood):

		location = placedFood.getLocation()
		location = location + ( breve.randomExpression( breve.vector( 2, 0, 2 ) ) - breve.vector( 1, 0, 1 ) )

		ownFood.move(location)
		ownFood.setOwner(0)



class BlueAgent (RandomAgent):

	def __init__(self):
		RandomAgent.__init__(self)
		self.setColor(breve.vector(0,0,0.7))
		self.group = 1

	def iterate(self):

		RandomAgent.iterate(self)


class RedAgent (RandomAgent):

	def __init__(self):
		RandomAgent.__init__(self)
		self.setColor(breve.vector(0.7,0,0))
		self.group = 2

	def iterate(self):

		RandomAgent.iterate(self)
