# import the pysb module and all its methods and functions
from pysb import *
from pysb import macros
import numpy as np
from pysb.simulator import ScipyOdeSimulator, BngSimulator
import matplotlib.pyplot as plt/Newcastle logo


# instantiate a model
Model()
# TODO: protein degradation to the system
# TODO: Use expression to control a few parameters

# declare monomers
Monomer('Proteins', ['b', 'folding'], {'folding': ['good', 'miss']})
# Monomer('MisP')
Monomer('ROS')
Monomer('HSP90', ['b'])
# Monomer('MCom')
Monomer('ATP')
Monomer('ADP')
Monomer('AggP')
Monomer('HSF1', ['b', 'b1', 'b2'])
# Monomer('HCom')
# Monomer('DiH')
# Monomer('TriH', ['b'])
Monomer('HSE', ['b', 'b1'])
# Monomer('HSE_TriH')
Monomer('Glutathione', ['state'], {'state': ['reduced','oxidised']})
Monomer('sHSP', ['b', 'position'], {'position': ['mito', 'non_mito']})
# Monomer('MisP_sHSP')
Monomer('MisP_sHSP_HSP90')
Monomer('OxyR', ['b', 'state'], {'state': ['active', 'inactive']})
Monomer('Glu_synthetase')
Monomer('Glu_reductase')
# Maybe we can merge this into 2
Monomer('sHSP_GluE')
# Monomer('sHSP_GluE_unbind')
# Might need this or might not
# Monomer('Glutathione_reductase')

# initial conditions (parameter + initial)
Parameter('NatP_0', 6000000)
Initial(Proteins(b=None,folding='good'), NatP_0)
Parameter('HSP90_0', 5900)
Initial(HSP90(b=None), HSP90_0)
Parameter('HSF1_0', 100)/Newcastle logo
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
Initial(sHSP_GluE(), sHSP_GluE_0)
Parameter('OxyR_0', 2000)
Initial(OxyR(b=None, state='inactive'), OxyR_0)

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
#####################################################
# TODO: CHECK What is happening with the Expression##
Observable('ROS_total', ROS())
# Parameter('m', 2)
# Expression('k20', (ROS_total * m))
#####################################################
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

# now input the rules
# Expression('NatP', k1)
# TODO: Every Reaction that synthesize protein needs to expend ATP
# TODO: Do we need to add OxyR production in the model as well
Rule('Protein_Sythesis', None >> Proteins(b=None, folding='good'), k1)
Rule('Misfolding', Proteins(b=None, folding='good') + ROS() >> Proteins(b=None, folding='miss') + ROS(), k2)
Rule('HSP90_MisP', Proteins(b=None, folding='miss') + HSP90(b=None) | Proteins(b=1, folding='miss') % HSP90(b=1), k3, k4)
Rule('Refolding', Proteins(b=1, folding='miss') % HSP90(b=1) + ATP() >> Proteins(b=None, folding='good') + HSP90(b=None) + ADP(), k6)
Rule('Aggregation', Proteins(b=None, folding='miss') + Proteins(b=None, folding='miss') >> AggP(), k7)
Rule('HSP90_HSF1', HSP90(b=None) + HSF1(b=None, b1=None, b2=None) | HSP90(b=1) % HSF1(b=1, b1=None, b2=None), k8, k9)
# Rule('Dimerisation', HSF1(b=None) + HSF1(b=None) | HSF1(b=1) % HSF1(b=1), k10, k12)
# macros.assemble_pore_sequential(HSF1, 'b1', 'b2', 3, [[k10, k12], [k11, k13]])
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
# Rule('Trimerisation', HSF1(b=None) + HSF1(b=1) % HSF1(b=1) | HSF1(b=2) % HSF1(b=1) % HSF1(b=1), k11, k13)
Rule('DNA_binding', HSF1(b1=2, b2=None) % HSF1(b1=2, b2=1) % HSF1(b1=None, b2=1) + HSE(b1=None) | HSF1(b1=2, b2=None) % HSF1(b1=2, b2=1) % HSF1(b1=3, b2=1) % HSE(b1=3), k14, k15)
# Assuming the transcription factor get of DNA after transcription & None basal Expression
# Try 2 different ways see if there is any difference
Rule('Transcription_Translation', HSF1(b1=2) % HSF1(b1=2, b2=1) % HSF1(b1=3, b2=1) % HSE(b1=3) >> HSF1(b=None, b1=None, b2=None) + HSF1(b=None, b1=None, b2=None) + HSF1(b=None, b1=None, b2=None) + HSE(b=None, b1=None) + HSP90(b=None), k16)

# TODO: Check which protein should be included in the degration part
# TODO: How to add stoichiometry to the rules
Rule('Degrades', HSP90(b=None) + ATP() + ATP() >> ADP(), k17)
# sHSP in both position gets degraded
Rule('Degrades_2', sHSP(b=None, position='mito') + ATP() >> ADP(), k17)
# Rule('Degrades', HSP90(b=None) + ATP() >> ADP(), k17)
Rule('ATP_generation', ADP() >> ATP(), k18)
Rule('cellular_processes', ATP() >> ADP(), k19)
Rule('ROS_production', None >> ROS(), k20)
Rule('ROS_scavenged', ROS() >> None, k21)

# Add on feature beneath
Rule('ROS_oxidation', ROS() + Glutathione(state='reduced') >> Glutathione(state='oxidised'), k22)
Rule('Glutathione_reduction', Glutathione(state='oxidised') >> Glutathione(state='reduced'), k34)
# Rule('ROS_oxidation_2',  >> , k22)
# Rightnow this is assuming no reverse
# Might change later
Rule('sHSP_binding', sHSP(b=None, position='mito') + Proteins(folding='miss') >> sHSP(b=None, position='mito') % Proteins(folding='miss'), k23)
Rule('sHSP_fail_to_hold', sHSP(b=None, position='mito') % Proteins(folding='miss') >> AggP(), k24)
Rule('HSP90_binding_on_MSP_sHSP', HSP90(b=None) + (sHSP(b=None, position='mito') % Proteins(b=None, folding='miss')) | HSP90(b=None) % sHSP(b=None, position='mito') % Proteins(b=None, folding='miss'), k25, k26)
Rule('Refolding_with_sHSP', HSP90(b=None) % sHSP(b=None, position='mito') % Proteins(b=None, folding='miss') >> Proteins(b=None, folding='good') + sHSP(b=None, position='mito') + HSP90(b=None), k27)
Rule('Activation_of_OxyR_by_ROS', OxyR(state='inactive') + ROS() >> OxyR(state='active') + ROS() ,k28)
# Subject to change with the addition of hill's equation
Rule('Active_OxyR_binding_DNA', OxyR(state='active') + sHSP_GluE() | OxyR(state='active') % sHSP_GluE() ,k32, k33)
Rule('sHSP_synthesis_from_DNA', sHSP_GluE() >> sHSP_GluE() + sHSP(b=None, position='non_mito'), k29)
# TODO: Make another paramter for the transfer later
Rule('sHSP_transfer', sHSP(b=None, position='non_mito') >> sHSP(b=None, position='mito'), k29)
Rule('Glutathione_Synthetase_synthesis_from_DNA', sHSP_GluE() >> sHSP_GluE() + Glu_synthetase(), k30)
Rule('Glu_Production', Glu_synthetase() >> Glu_synthetase() + Glutathione(state='reduced'), k31)





# Observables
Observable('NatP', Proteins(folding='good'))
Observable('MisP', Proteins(folding='miss'))/Newcastle logo)
# sim = StochKitSimulator(model, tspan=np.linspace(0, 10, 5))sim = BngSimulator(model)
sim = BngSimulator(model)
simres = sim.run(tspan=t, verbose=False, initials={ATP(): 0})

yout = simres.all

fig, axs = plt.subplots(3, 1)

axs[0].plot(t, yout['NatP'], label="NatP")
axs[0].plot(t, yout['MisP'], label="MisP")
axs[0].plot(t, yout['obsMCom'], label="MisP/Hsp90 complex")
axs[0].plot(t, yout['obsAggP'], label="AggP")
axs[0].plot(t, yout['obsHSP90'], label="HSP90")
axs[0].legend()
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Number of Molecules")

axs[1].plot(t, yout['obsATP'], label="ATP")
axs[1].plot(t, yout['obsADP'], label="ADP")
axs[1].plot(t, yout['obsROS'], label="ROS")
axs[1].legend()
axs[1].set_xlabel("Time (s)")
axs[1].set_ylabel("Number of Molecules")
# axs[1].savefig('b.png')

axs[2].plot(t, yout['obssHSP'], label="sHSP")
axs[2].plot(t, yout['obsGlutathionine'], label="Glutathionine")
axs[2].legend()


fig.savefig('graph.png')
