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
Monomer('HSF1')
Monomer('DiH')
Monomer('TriH')
Monomer('HSE')
Monomer('HSE_TriH')

# input the parameter values
Parameter('k1', 10) # mol s^-1
Parameter('k2', 0.00002) # mol^-1 s^-1
Parameter('k3', 50.0)
Parameter('k4', 0.00001)
Parameter('k11', 10)
Parameter('k12', 0.5)
Parameter('k11', 10)
Parameter('k14', 0.05)
Parameter('k15', 0.08)

# now input the rules
# Expression('NatP', k1)
Rule('Protein_Sythesis', None >> Proteins(folding='good'), k1)
Rule('Misfolding', Proteins(folding='good') + ROS() >> Proteins(folding='miss') + ROS(), k2)
Rule('HSP90_MisP', Proteins(folding='miss') + HSP90() | MCom(), k3, k4)
Rule('Trimerisation', HSF1() + DiH() | TriH, k11, k12)
Rule('DNA_binding', TriH() + HSE() | HSE_TriH(), )

# initial conditions (parameter + initial)
Parameter('NatP_0', 6000000)
Initial(Proteins(folding='good'), NatP_0)
Parameter('ROS_0', 100)
Initial(ROS(), ROS_0)
Parameter('HSF1_0', 100)
Initial(HSF1(), HSF1_0)
Parameter('DiH_0', 0)
Initial(DiH(),DiH_0)


# Observables
Observable('NatP', Proteins(folding='good'))
Observable('HSF1_1', HSF1())


