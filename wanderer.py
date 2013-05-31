import breve
import math
import random

default_wander_range = 20
wander_time_limit = 100
wander_max_velocity = 6

class WanderingAgent (breve.Mobile):
	def __init__(self):
		breve.Mobile.__init__(self)
		
		# Just to define that there's a wanderRange
		self.wanderRange = breve.vector()

		# Set initial position to random
		self.randomizeLocation()

		# Set random wander time so not all agents switch wandering targets at the same time
		self.wanderTime = random.randint(0, wander_time_limit)
		self.setNewRandomWanderTarget()

		print "Created Wandering agent"

	def iterate(self):
		# Increase the wander time
		self.wanderTime += 1

		# If the agent is close to its goal or has been chasing its current goal for a long time, pick a new target to go to
		if(dist(self.getLocation(), self.wanderTarget) < 4 or self.wanderTime > wander_time_limit):
			self.wanderTime = 0
			self.setNewRandomWanderTarget()

		# Calculate the optimal, normalised velocity if the agent were to go directly to his goal
		desiredVelocity = normalizeVector(self.accelerationTowardsFocus(self.wanderTarget)) * wander_max_velocity

		# Calculate by how much the agent adjust's its current course
		steeringVector = (desiredVelocity - self.getVelocity())/10

		# Update an agent's speed
		self.setVelocity(truncate(self.getVelocity() + steeringVector, wander_max_velocity))

	def accelerationTowardsFocus(self, focus):
		return (focus - self.getLocation())/1

	def randomizeLocation(self):
		randomLoc = breve.randomExpression( 2*breve.vector( self.wanderRange.x, self.wanderRange.y, self.wanderRange.z) )  - breve.vector( 
					self.wanderRange.x, self.wanderRange.y, self.wanderRange.z )
		self.move(randomLoc)

	def setWanderRange(self, newWanderRange):
		self.wanderRange = newWanderRange
		self.setNewRandomWanderTarget()

	def setNewRandomWanderTarget(self):
		self.wanderTarget = breve.randomExpression( 2*breve.vector( self.wanderRange.x, self.wanderRange.y, self.wanderRange.z) )  - breve.vector( 
					self.wanderRange.x, self.wanderRange.y, self.wanderRange.z )


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