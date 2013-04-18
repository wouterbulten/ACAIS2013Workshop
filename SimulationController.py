import breve

class SimulationController ( breve.Control ):

        def __init__( self ):
                breve.Control.__init__(self)

                print "Simulation Started"

        def iterate( self ):

                breve.Control.iterate( self )

# Start the simulation
SimulationController()