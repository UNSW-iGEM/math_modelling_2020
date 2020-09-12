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
Monomer('ADP')
Monomer('AggP')
Monomer('HSF1')
Monomer('HCom')
Monomer('DiH')


# input the parameter values
Parameter('k1', 10) # mol s^-1
Parameter('k2', 0.00002) # mol^-1 s^-1
Parameter('k3', 50.0)
Parameter('k4', 0.00001)
Parameter('k5', 4*10**-6)
Parameter('k6', 6*10**-7)
Parameter('k7', 10**-7)
Parameter('k8', 500)
Parameter('k9', 1)
Parameter('k10', 0.01)

# now input the rules
# Expression('NatP', k1)
Rule('Protein_Sythesis', None >> Proteins(folding='good'), k1)
Rule('Misfolding', Proteins(folding='good') + ROS() >> Proteins(folding='miss') + ROS(), k2)
Rule('HSP90_MisP', Proteins(folding='miss') + HSP90() | MCom(), k3, k4)
Rule('Refolding', MCom() + ATP() >> Proteins(folding='good') + HSP90() + ADP(), k6)
Rule('Aggregation', Proteins(folding='miss') + Proteins(folding='miss') >> AggP(), k7)
Rule('HSP90_HSF1', HSP90() + HSF1() | HCom(), k8, k9)
Rule('Dimerisation', HSF1() + HSF1() >> DiH(), k10)



# initial conditions (parameter + initial)
Parameter('NatP_0', 6000000)
Initial(Proteins(folding='good'), NatP_0)
Parameter('HSP90_0', 5900)
Initial(HSP90(), HSP90_0)
Parameter('HSF1_0', 100)
Initial(HSF1(), HSF1_0)
Parameter('ROS_0', 100)
Initial(ROS(), ROS_0)
Parameter('ATP_0', 10000)
Initial(ATP(), ATP_0)
Parameter('ADP_0', 1000)
Initial(ADP(), ADP_0)
Parameter('HSE_0', 1)
Initial(HSE(), HSE_0)


# Observables
Observable('NatP', Proteins(folding='good'))
Observable('MisP', Proteins(folding='miss'))
Observable('MCom', MCom())
Observable('AggP', AggP())
Observable('HSP90', HSP90())
# total hsp90

Observable('ATP', ATP())
Observable('ADP', ADP())
Observable('ROS', ROS())
