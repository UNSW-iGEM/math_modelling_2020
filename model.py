# import the pysb module and all its methods and functions
from pysb import *

# instantiate a model
Model()

# declare monomers
Monomer('Proteins', ['folding'], {'folding': ['good', 'miss']})
# Monomer('MisP')
Monomer('ROS')
Monomer('HSP90')
Monomer('MCom')
Monomer('ATP')


# input the parameter values
Parameter('k1', 10) # mol s^-1
Parameter('k2', 0.00002) # mol^-1 s^-1
Parameter('k3', 50.0)
Parameter('k4', 0.00001)

# now input the rules
# Expression('NatP', k1)
Rule('Protein_Sythesis', None >> Proteins(folding='good'), k1)
Rule('Misfolding', Proteins(folding='good') + ROS() >> Proteins(folding='miss') + ROS(), k2)
Rule('HSP90&MisP', Proteins(folding='miss') + HSP90() | MCom(), k3, k4)

# initial conditions (parameter + initial)
Parameter('NatP_0', 6000000)
Initial(Proteins(folding='good'), NatP_0)
Parameter('ROS_0', 100)
Initial(ROS(), ROS_0)


# Observables
Observable('NatP', Proteins(folding='good'))
