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
Monomer('TriH')
Monomer('HSE')
Monomer('HSE_TriH')
Monomer('Glutathiione', ['state'], {'state': ['reduced','oxidised']})
Monomer('sHSP')
Monomer('MisP_sHSP')
Monomer('MisP_sHSP_HSP90')
Monomer('OxyR', ['state', {'active', 'inactive'}])
Monomer('sHSP_GluE')

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
Parameter('k11', 100)
Parameter('k12', 0.5)
Parameter('k13', 0.5)
Parameter('k14', 0.05)
Parameter('k15', 0.08)
Parameter('k16', 1000)
Parameter('k17', 8.02*10**-9)
Parameter('k18', 12)
Parameter('k19', 0.02)
Parameter('k20', 0.1)
Parameter('k21', 0.001)
# This value still needs to be changed
Parameter('k22', 0.002)
Parameter('k23', 50.0)
Parameter('k24', 10.0)
Parameter('k25', 50.0)
Parameter('k26', 5.0)
Parameter('k27', 10.0)
Parameter('k28', 20.0)
Parameter('k29', 10.0)
Parameter('k30', 10.0)
Parameter('k31', 5.0)
Parameter('K32', 20.0)


# now input the rules
# Expression('NatP', k1)
Rule('Protein_Sythesis', None >> Proteins(folding='good'), k1)
Rule('Misfolding', Proteins(folding='good') + ROS() >> Proteins(folding='miss') + ROS(), k2)
Rule('HSP90_MisP', Proteins(folding='miss') + HSP90() | MCom(), k3, k4)
Rule('Refolding', MCom() + ATP() >> Proteins(folding='good') + HSP90() + ADP(), k6)
Rule('Aggregation', Proteins(folding='miss') + Proteins(folding='miss') >> AggP(), k7)
Rule('HSP90_HSF1', HSP90() + HSF1() | HCom(), k8, k9)
Rule('Dimerisation', HSF1() + HSF1() | DiH(), k10, k12)
Rule('Trimerisation', HSF1() + DiH() | TriH, k11, k13)
Rule('DNA_binding', TriH() + HSE() | HSE_TriH(), k14, k15)
Rule('Transcription', HSE_TriH() >> HSE_TriH() + HSP90(), k16)
Rule('Degrades', HSP90() + ATP() >> ADP(), k17)
Rule('ATP_generation', ADP() >> ATP(), k18)
Rule('cellular_processes', ATP() >> ADP(), k19)
Rule('ROS_production', None >> ROS(), k20)
Rule('ROS_scavenged', ROS() >> None, k21)
# Add on feature beneath
# Need to combine the 2 reaction later
Rule('ROS_oxidation', ROS() >> None, k22)
Rule('ROS_oxidation_2', Glutathiione(state='reduced') >> Glutathiione(state='oxidised'), k22)
# Rightnow this is assuming no reverse
# Might change later
Rule('sHSP_binding', sHSP() + Protein(folding='miss') >> MisP_sHSP, k23)
Rule('sHSP_fail_to_hold', Mis_P_sHSP() >> AggP(), k24)
Rule('HSP90_binding_on_MSP_sHSP', HSP90() + MisP_sHSP() | MisP_sHSP_HSP90(), k25, k26)
Rule('Refolding_with_sHSP', MisP_sHSP_HSP90() >> NatP() + sHSP() + HSP90(), k27)
Rule('Activation_of_OxyR_by_ROS', )

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
Observable('obsMCom', MCom())
Observable('obsAggP', AggP())
Observable('obsHSP90', HSP90())
# total hsp90
Observable('obsATP', ATP())
Observable('obsADP', ADP())
Observable('obsROS', ROS())
