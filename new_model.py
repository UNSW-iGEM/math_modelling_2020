# import the pysb module and all its methods and functions
from pysb import *
from pysb import macros

# instantiate a model
Model()
# TODO: protein degradation to the system
# TODO: Use expression to control a few parameters

# declare monomers
Monomer('Proteins', ['b', 'Hbind' , 'folding'], {'folding': ['good', 'miss']})
Monomer('ROS')
Monomer('HSP90', ['b', 'Hbind'])
Monomer('ATP')
Monomer('ADP')
Monomer('AggP')
Monomer('HSF1', ['b', 'b1', 'b2'])
Monomer('HSE', ['b', 'b1'])
Monomer('Glutathione', ['state'], {'state': ['reduced','oxidised']})
Monomer('sHSP', ['b', 'position'], {'position': ['mito', 'non_mito']})
Monomer('MisP_sHSP_HSP90')
Monomer('OxyR', ['DNA', 'state'], {'state': ['active', 'inactive']})
Monomer('Glu_synthetase')
Monomer('Glu_reductase')
# Maybe we can merge this into 2
Monomer('sHSP_GluE', ['DNA'])
# Might need this or might not

# initial conditions (parameter + initial)
Parameter('NatP_0', 6000000)
Initial(Proteins(b=None, Hbind=None, folding='good'), NatP_0)
Parameter('HSP90_0', 5900)
Initial(HSP90(b=None, Hbind=None), HSP90_0)
Parameter('HSF1_0', 100)
Initial(HSF1(b=None, b1=None, b2=None), HSF1_0)
Parameter('ROS_0', 100)
Initial(ROS(), ROS_0)
Parameter('ATP_0', 10000)
Initial(ATP(), ATP_0)
Parameter('ADP_0', 1000)
Initial(ADP(), ADP_0)
Parameter('HSE_0', 1)
Initial(HSE(b=None, b1=None), HSE_0)
# sHSP + Glu + sHSP_GluE + OxyR
Parameter('sHSP_0', 2000)
Initial(sHSP(b=None, position='mito'), sHSP_0)
Parameter('Glutathione_0', 2000)
Initial(Glutathione(state='reduced'), Glutathione_0)
Initial(Glutathione(state='oxidised'), Glutathione_0)
Parameter('sHSP_GluE_0', 2)
Initial(sHSP_GluE(DNA=None), sHSP_GluE_0)
Parameter('OxyR_0', 2000)
Initial(OxyR(DNA=None, state='inactive'), OxyR_0)

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
Parameter('k22', 20)
Parameter('k23', 50.0)
Parameter('k24', 1.0)
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
# This should be a relatively small value
Parameter('k34', 0.01)
Parameter('k35', 0.8)
Parameter('k36', 0.2)

# now input the rules
# TODO: Every Reaction that synthesize protein needs to expend ATP
# TODO: Do we need to add OxyR production in the model as well
Rule('Protein_Sythesis', ATP() >> Proteins(b=None, Hbind=None, folding='good') + ADP(), k1)
Rule('Misfolding', Proteins(b=None, Hbind=None, folding='good') + ROS() >> Proteins(b=None, Hbind=None, folding='miss') + ROS(), k2)
Rule('HSP90_MisP', Proteins(b=None, Hbind=None, folding='miss') + HSP90(b=None, Hbind=None) | Proteins(b=None, Hbind=1, folding='miss') % HSP90(b=None, Hbind=1), k3, k4)
Rule('Refolding', Proteins(b=None, Hbind=1, folding='miss') % HSP90(b=None, Hbind=1) + ATP() >> Proteins(b=None, Hbind=None, folding='good') + HSP90(b=None, Hbind=None) + ADP(), k5)
Rule('Protein_degradation', Proteins(folding='miss') + ATP() >> ADP(), k6)
Rule('Aggregation', Proteins(b=None, folding='miss') + Proteins(b=None, folding='miss') >> AggP(), k7)
Rule('HSP90_HSF1', HSP90(b=None, Hbind=None) + HSF1(b=None, b1=None, b2=None) | HSP90(b=1, Hbind=None) % HSF1(b=1, b1=None, b2=None), k8, k9)
Rule('Dimerize',
      HSF1(b1=None, b2=None) + HSF1(b1=None, b2=None) |
          HSF1(b1=None, b2=1) % HSF1(b1=None, b2=1),
      k10,
      k12)
Rule('Trimerize',
      HSF1(b1=None, b2=None) + HSF1(b1=None, b2=1) % HSF1(b1=None, b2=1) |
          HSF1(b1=2, b2=None) % HSF1(b1=2, b2=1) % HSF1(b1=None, b2=1),
      k11,
      k13)
Rule('DNA_binding', HSF1(b1=2, b2=None) % HSF1(b1=2, b2=1) % HSF1(b1=None, b2=1) + HSE(b1=None) | 
            HSF1(b1=2, b2=None) % HSF1(b1=2, b2=1) % HSF1(b1=3, b2=1) % HSE(b1=3), k14, k15)
# Assuming the transcription factor get of DNA after transcription & None basal Expression
# Try 2 different ways see if there is any difference
Rule('Transcription_Translation', HSF1(b1=2) % HSF1(b1=2, b2=1) % HSF1(b1=3, b2=1) % HSE(b1=3) >> 
    HSF1(b=None, b1=None, b2=None) + HSF1(b=None, b1=None, b2=None) + HSF1(b=None, b1=None, b2=None) 
    + HSE(b=None, b1=None) + HSP90(b=None, Hbind=None), k16)

# TODO: Check which protein should be included in the degration part
# TODO: How to add stoichiometry to the rules
Rule('Degrades', HSP90(b=None, Hbind=None) + ATP() + ATP() >> ADP() + ADP(), k17)
# Only accounting the degradation of sHSP in mito
Rule('Degrades_2', sHSP(b=None, position='mito') + ATP() >> ADP(), k17)
# Rule('Degrades', HSP90(b=None) + ATP() >> ADP(), k17)
Rule('ATP_generation', ADP() >> ATP(), k18)
Rule('cellular_processes', ATP() >> ADP(), k19)
Rule('ROS_production', None >> ROS(), k20)
Rule('ROS_scavenged', ROS() >> None, k21)

# Add on feature beneath
Rule('ROS_oxidation', ROS() + Glutathione(state='reduced') >> Glutathione(state='oxidised'), k22)
Rule('Glutathione_reduction', Glutathione(state='oxidised') >> Glutathione(state='reduced'), k34)

Rule('sHSP_binding', sHSP(b=None, position='mito') + Proteins(b=None, Hbind=None, folding='miss') | sHSP(b=1, position='mito') % Proteins(b=1, Hbind=None, folding='miss'), k23, k36)
Rule('sHSP_fail_to_hold', sHSP(b=1, position='mito') % Proteins(b=1, Hbind=None, folding='miss') >> AggP(), k24)
Rule('HSP90_binding_on_MSP_sHSP', HSP90(b=None, Hbind=None) + (sHSP(b=1, position='mito') % Proteins(b=1, Hbind=None, folding='miss')) | HSP90(b=None, Hbind=2) % Proteins(b=1, Hbind=2, folding='miss') % sHSP(b=1, position='mito'), k25, k26)
Rule('Refolding_with_sHSP', HSP90(b=None, Hbind=2) % Proteins(b=1, Hbind=2, folding='miss') % sHSP(b=1, position='mito') + ATP() >> 
                        Proteins(b=None, Hbind=None, folding='good') + sHSP(b=None, position='mito') + HSP90(b=None, Hbind=None) + ADP(), k27)
Rule('Activation_of_OxyR_by_ROS', OxyR(state='inactive') + ROS() >> OxyR(state='active') + ROS() ,k28)
Rule('Active_OxyR_binding_DNA', OxyR(DNA=None, state='active') + sHSP_GluE(DNA=None) | OxyR(DNA=1, state='active') % sHSP_GluE(DNA=1) ,k32, k33)
Rule('sHSP_synthesis_from_DNA',OxyR(DNA=1, state='active') % sHSP_GluE(DNA=1) >> sHSP_GluE(DNA=None) + sHSP(b=None, position='non_mito') + OxyR(DNA=None, state='active'), k29)
# This is done because the sHSP is targeting at a specific region the cell namely the mitochondria
Rule('sHSP_transfer', sHSP(b=None, position='non_mito') >> sHSP(b=None, position='mito'), k35)
Rule('Glutathione_Synthetase_synthesis_from_DNA', OxyR(DNA=1, state='active') % sHSP_GluE(DNA=1) >> 
                        sHSP_GluE(DNA=None) + OxyR(DNA=None, state='active') + Glu_synthetase(), k30)
Rule('Glu_Production', Glu_synthetase() >> Glu_synthetase() + Glutathione(state='reduced'), k31)


# Observables
Observable('NatP', Proteins(folding='good'))
Observable('MisP', Proteins(folding='miss'))
Observable('obsMCom', Proteins(folding='miss') % HSP90())
Observable('obsAggP', AggP())
Observable('obsHSP90', HSP90())
# total hsp90
Observable('obsATP', ATP())
Observable('obsADP', ADP())
Observable('obsROS', ROS())

Observable('obssHSP', sHSP(b=None, position='mito'))
Observable('obsMisP_sHSP', sHSP(b=1) % Proteins(b=1,folding='miss'))
Observable('obsMisP_sHSP_HSP90', HSP90() % sHSP(b=1) % Proteins(b=1, folding='miss'))
Observable('obsGlutathionine', Glutathione(state='oxidised'))