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
Monomer('Glutathione', ['state'], {'state': ['reduced','oxidised']})
Monomer('sHSP')
Monomer('MisP_sHSP')
Monomer('MisP_sHSP_HSP90')
Monomer('OxyR', ['state'], {'state': ['active', 'inactive']})
Monomer('Glu_synthetase')
# Maybe we can merge this into 2
Monomer('sHSP_GluE')
Monomer('sHSP_GluE_unbind')

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
Parameter('k32', 20.0)
# Might remove this parameter later since this is the reverse
# of the binding
Parameter('k33', 25.0)

# now input the rules
# Expression('NatP', k1)
# TODO: Every Reaction that synthesize protein needs to expend ATP
Rule('Protein_Sythesis', None >> Proteins(folding='good'), k1)
Rule('Misfolding', Proteins(folding='good') + ROS() >> Proteins(folding='miss') + ROS(), k2)
Rule('HSP90_MisP', Proteins(folding='miss') + HSP90() | MCom(), k3, k4)
Rule('Refolding', MCom() + ATP() >> Proteins(folding='good') + HSP90() + ADP(), k6)
Rule('Aggregation', Proteins(folding='miss') + Proteins(folding='miss') >> AggP(), k7)
Rule('HSP90_HSF1', HSP90() + HSF1() | HCom(), k8, k9)
Rule('Dimerisation', HSF1() + HSF1() | DiH(), k10, k12)
Rule('Trimerisation', HSF1() + DiH() | TriH, k11, k13)
Rule('DNA_binding', TriH() + HSE() | HSE_TriH(), k14, k15)
Rule('Transcription_Translation', HSE_TriH() >> HSE_TriH() + HSP90(), k16)
Rule('Degrades', HSP90() + ATP() >> ADP(), k17)
Rule('ATP_generation', ADP() >> ATP(), k18)
Rule('cellular_processes', ATP() >> ADP(), k19)
Rule('ROS_production', None >> ROS(), k20)
Rule('ROS_scavenged', ROS() >> None, k21)
# Add on feature beneath
# Need to combine the 2 reaction later
Rule('ROS_oxidation', ROS() >> None, k22)
Rule('ROS_oxidation_2', Glutathione(state='reduced') >> Glutathione(state='oxidised'), k22)
# Rightnow this is assuming no reverse
# Might change later
Rule('sHSP_binding', sHSP() + Proteins(folding='miss') >> MisP_sHSP, k23)
Rule('sHSP_fail_to_hold', MisP_sHSP() >> AggP(), k24)
Rule('HSP90_binding_on_MSP_sHSP', HSP90() + MisP_sHSP() | MisP_sHSP_HSP90(), k25, k26)
Rule('Refolding_with_sHSP', MisP_sHSP_HSP90() >> Proteins(folding='good') + sHSP() + HSP90(), k27)
Rule('Activation_of_OxyR_by_ROS', OxyR(state='inactive') >> OxyR(state='active') ,k28)
# Subject to change with the addition of hill's equation
Rule('Active_OxyR_binding_DNA', OxyR(state='active') + sHSP_GluE_unbind() | sHSP_GluE() ,k32, k33)
Rule('sHSP_synthesis_from_DNA', sHSP_GluE() >> sHSP_GluE() + sHSP(), k29)
Rule('Glutathione_Synthetase_synthesis_from_DNA', sHSP_GluE() >> sHSP_GluE() + Glu_synthetase(), k30)
Rule('Glu_Production', Glu_synthetase() >> Glu_synthetase() + Glutathione(state='reduced'), k31)


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
# sHSP + Glu + sHSP_GluE + OxyR
Parameter('sHSP_0', 2000)
Initial(sHSP(), sHSP_0)
Parameter('Glutathione_0', 2000)
Initial(Glutathione(state='reduced'), Glutathione_0)
Parameter('sHSP_GluE_0', 2)
Initial(sHSP_GluE_unbind(), sHSP_GluE_0)
Parameter('OxyR_0', 2000)
Initial(OxyR(state='inactive'), OxyR_0)



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
