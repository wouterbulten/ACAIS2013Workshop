import food
import breve
import wanderer


class SimpleAgent (breve.Mobile):

	def __init__(self):
		breve.Mobile.__init__(self)

		print "Created agent"

	def iterate(self):
		None


class RandomAgent (wanderer.WanderingAgent):

	def __init__(self):
		wanderer.WanderingAgent.__init__(self)

		# Set the wander range of the agent
		self.setWanderRange(breve.vector(20.0, 20.0, 20.0))

		# Set the shape of the agent
		self.setShape(self.controller.getAgentShape())

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

		wanderer.WanderingAgent.iterate(self)

	def collisionWithFood(self, f):
		
		if(f.getOwner()):
			return

		# We want two iterations without an collision
		if(self.collidedTimer > 0):
			self.collidedTimer = 2

		# Set the timer for the collision
		self.collidedTimer = 2

		if(self.carrying != None):

			if(self.carrying.getGroup() != f.getGroup() and f.getGroup() != 0):
				return

			self.placeFoodObject(self.carrying, f)
			self.carrying = None
			return

		self.carrying = f
		self.carrying.setOwner(self)
		self.carrying.setColor(self.getColor())
		self.carrying.setGroup(self.group)

	def placeFoodObject(self, ownFood, placedFood):

		location = placedFood.getLocation()
		location = location + ( breve.randomExpression( breve.vector( 2, 2, 2 ) ) - breve.vector( 1, 1, 1 ) )

		ownFood.move(location)
		ownFood.setOwner(0)



class BlueAgent (RandomAgent):
	def __init__(self):
		RandomAgent.__init__(self)
		self.setColor(breve.vector(0.2,0.2,0.8))
		self.group = 1

	def iterate(self):
		RandomAgent.iterate(self)


class RedAgent (RandomAgent):
	def __init__(self):
		RandomAgent.__init__(self)
		self.setColor(breve.vector(0.8,0.2,0.2))
		self.group = 2

	def iterate(self):
		RandomAgent.iterate(self)
