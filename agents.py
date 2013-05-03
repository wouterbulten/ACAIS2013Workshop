import breve
import math
import agents

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

		print "Created agent"

	def iterate(self):
		breve.Wanderer.iterate(self)

# perhaps put at least the wander_distance limit in a config file or something?
wander_distance_limit = 10
wander_time_limit = 100
wander_max_velocity = 2

class WanderingAgent (breve.Wanderer):
	def __init__(self):
		breve.Wanderer.__init__(self)

		self.setWanderRange(breve.vector(wander_distance_limit, 0, wander_distance_limit))

		# Set the shape of the agent
		cube = breve.createInstances(breve.Cube, 1).initWith(breve.vector(1,1,1))
		self.setShape(cube)

		# Set initial position to random
		self.randomizeLocation()

		self.wanderTime = 0
		self.wanderTarget = breve.randomExpression( 
					breve.vector( wander_distance_limit*2 , 0, wander_distance_limit*2 ) )  - breve.vector( 
					wander_distance_limit, 0, wander_distance_limit )

		print "Created Wandering agent"

	def iterate(self):
### Enable if the agents run act increasingly weirder and go increasingly faster out of map range
#		if(abs(self.getLocation().x) > (agents.wander_distance_limit - 50) or abs(self.getLocation().z) > (agents.wander_distance_limit - 50)):
#				self.wanderTime = 0
#				self.wanderTarget = breve.randomExpression( 
#						breve.vector( agents.wander_distance_limit*2 , 0, agents.wander_distance_limit*2 ) )  - breve.vector( 
#						agents.wander_distance_limit, 0, agents.wander_distance_limit )
#
#				#print 'resetting wanderTarget due to location becoming out of reach for an agent'
#				self.setAcceleration(breve.vector())
#				self.setVelocity(breve.vector())

		if(self.wanderTime > wander_time_limit or agents.dist(self.getLocation(), self.wanderTarget) < 2):
			self.wanderTarget = breve.randomExpression( 
					breve.vector( wander_distance_limit*2 , 0, wander_distance_limit*2 ) )  - breve.vector( 
					wander_distance_limit, 0, wander_distance_limit )
			self.wanderTime = 0

		desiredVelocity = agents.normalizeVector(self.accelerationTowardsFocus(self.wanderTarget)) * agents.wander_max_velocity
		steeringVector = desiredVelocity - self.getVelocity()

		self.setVelocity(agents.truncate(self.getVelocity() + steeringVector), agents.wander_max_velocity)
		#self.setVelocity(breve.vector(1, 0, 1))

		self.wanderTime += 1

		print 'iterating agent'

	def accelerationTowardsFocus(self, focus):
		return (focus - self.getLocation())



####### Help functions for the wanderer
def dist(v1, v2):
	return math.sqrt(math.pow(v1.x - v2.x, 2) + math.pow(v1.y - v2.y, 2) + math.pow(v1.z - v2.y, 2))

def normalizeVector(vector):
	lengthVector = breve.length(vector)

	if(lengthVector == 0):
		return vector

	vector.x = vector.x / lengthVector
	vector.y = vector.y / lengthVector
	vector.z = vector.z / lengthVector


def truncate(vector, max):
	i = max / breve.length(vector)

	if (i < 1.0):
		i = 1.0

	return scaleVector(vector, i)

def scaleVector(vector, scale):
	vector.x = vector.x *scale
	vector.y = vector.y * scale
	vector.z = vector.z * scale

	return vector