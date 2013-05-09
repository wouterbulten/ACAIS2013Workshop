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

            breve.createInstances(agents.BlueAgent, 50)
            breve.createInstances(agents.RedAgent, 50)

            # Speeds up the simulation but makes it less accurate
            self.setIntegrationStep( 0.05 )

            print "Simulation Started"

        def iterate( self ):

        	#Optional: Make the simulation run a bit slower
			#self.sleep(0.02)
			
			breve.Control.iterate(self)

# Start the simulation
SimulationController()