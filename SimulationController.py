import breve
import food
import agents
import wanderer

class SimulationController ( breve.Control ):

        def __init__( self ):
            breve.Control.__init__(self)

            # Create a floor for the world
            self.floor = breve.Floor()
            self.floor.setTextureImage(None)
            self.floor.move(breve.vector(0, -23, 0))

            self.cameraViewDepth             = 1700          # How far the camera can see
            self.cameraViewPoint             = breve.vector( 100, 21, -4.8 )
            self.pointCamera( breve.vector( 0, 0, 0 ), self.cameraViewPoint )
            # Increase viewing depth
            self.setZClip(self.cameraViewDepth)


            # Create a shape for the agents
            self.agentShape = breve.createInstances(breve.Cube, 1).initWith(breve.vector(1,1,1))
            # Create a shape for the food sources
            self.foodShape = breve.createInstances(breve.Sphere, 1).initWith(0.5)

            # Set display settings
            self.enableLighting()
            #self.enableShadows()
            #self.moveLight(breve.vector(80,100,0))
            #self.enableReflections()
            #self.enableSmoothDrawing()

            breve.createInstances(food.SimpleFood, 800)
            # Create agents
            #self.agent = agents.SimpleAgent()
            #self.randomAgent = agents.RandomAgent()

            breve.createInstances(wanderer.WanderingAgent, 100)
            #breve.createInstances(agents.BlueAgent, 50)
            #breve.createInstances(agents.RedAgent, 50)

            # Speeds up the simulation but makes it less accurate
            self.setIntegrationStep( 0.05 )

            print "Simulation Started"

        def iterate( self ):

        	#Optional: Make the simulation run a bit slower
			#self.sleep(0.02)
			
			breve.Control.iterate(self)


        def getAgentShape(self):
            return self.agentShape

        def getFoodShape(self):
            return self.foodShape

# Start the simulation
SimulationController()