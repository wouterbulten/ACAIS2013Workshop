import breve
import agents

class SimulationController ( breve.Control ):

        def __init__( self ):
            breve.Control.__init__(self)

            # Create a floor for the world
            self.floor = breve.Floor()
            self.floor.setTextureImage(None)

            # Set display settings
            self.enableLighting()
            self.enableShadows()
            self.moveLight(breve.vector(80,100,0))
            self.enableReflections()
            self.enableSmoothDrawing()

            # Create agents
            self.agent = agents.SimpleAgent()

            print "Simulation Started"

        def iterate( self ):

            breve.Control.iterate( self )

# Start the simulation
SimulationController()