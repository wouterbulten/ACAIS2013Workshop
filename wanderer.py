import breve
import math
import random

# perhaps put at least the wander_distance limit in a config file or something?
wander_distance_limit = 20
wander_time_limit = 125
wander_max_velocity = 5

class WanderingAgent (breve.Wanderer):
	def __init__(self):
		breve.Wanderer.__init__(self)

		self.setWanderRange(breve.vector(wander_distance_limit, 0, wander_distance_limit))

		# Set the shape of the agent
		cube = breve.createInstances(breve.Cube, 1).initWith(breve.vector(1,1,1))
		self.setShape(cube)

		# Set initial position to random
		self.randomizeLocation()

		self.wanderTime = random.randint(0, wander_time_limit)
		self.wanderTarget = breve.randomExpression( 
					2*breve.vector( wander_distance_limit, wander_distance_limit, wander_distance_limit) )  - breve.vector( 
					wander_distance_limit, wander_distance_limit, wander_distance_limit )

		print "Created Wandering agent"

	def iterate(self):
	# Enable if the agents run act increasingly weirder and go increasingly faster out of map range
		if(abs(self.getLocation().x) > (wander_distance_limit) or abs(self.getLocation().z) > (wander_distance_limit) or abs(self.getLocation().y > (wander_distance_limit))):
				self.wanderTime = 0
				self.wanderTarget = breve.randomExpression( 
						breve.vector( wander_distance_limit*2 , wander_distance_limit*2, wander_distance_limit*2 ) )  - breve.vector( 
						wander_distance_limit, wander_distance_limit, wander_distance_limit )

				#print 'resetting wanderTarget due to location becoming out of reach for an agent'
				#self.setAcceleration(breve.vector())
				#self.setVelocity(breve.vector())

		#helping the above bit if it really gets out of hand
		if(abs(self.getLocation().x) > (wander_distance_limit*2) or abs(self.getLocation().z) > (wander_distance_limit*2) or abs(self.getLocation().y > (wander_distance_limit*2))):
				#print 'resetting wanderTarget due to location becoming out of reach for an agent'
				self.setAcceleration(breve.vector())
				self.setVelocity(breve.vector())

		self.wanderTime += 1
		if(dist(self.getLocation(), self.wanderTarget) < 5 or self.wanderTime > wander_time_limit):
			self.wanderTime = 0
			self.wanderTarget = breve.randomExpression( 
					breve.vector( wander_distance_limit*2, wander_distance_limit*2, wander_distance_limit*2 ) )  - breve.vector( 
					wander_distance_limit, wander_distance_limit, wander_distance_limit)

				#print 'wander focus set for agent ' + str(self.agentId) + ' to ' + str(self.wanderFocus.x) + ', ' + str(self.wanderFocus.z)

		desiredVelocity = normalizeVector(self.accelerationTowardsFocus(self.wanderTarget)) * wander_max_velocity
		steeringVector = (desiredVelocity - self.getVelocity())/10

		self.setVelocity(truncate(self.getVelocity() + steeringVector, wander_max_velocity))

	def accelerationTowardsFocus(self, focus):
		return (focus - self.getLocation())/1



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
	
	return vector


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