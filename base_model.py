from pysb import *
from pysb import macros
from util import produceGraph, tempValues

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
#############################################################
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

Parameter('k1', 10) # mol s^-1
Rule('Protein_Sythesis', ATP() >> Proteins(b=None, Hbind=None, folding='good') + ADP(), k1)
Parameter('k2', 0.00002) # mol^-1 s^-1
Rule('Misfolding', Proteins(b=None, Hbind=None, folding='good') + ROS() >>
                Proteins(b=None, Hbind=None, folding='miss') + ROS(), k2)
Parameter('k3', 50.0)
Parameter('k4', 0.00001)
Rule('HSP90_MisP', Proteins(b=None, Hbind=None, folding='miss') + HSP90(b=None, Hbind=None) |
                Proteins(b=None, Hbind=1, folding='miss') % HSP90(b=None, Hbind=1), k3, k4)
Parameter('k5', 4*10**-6)
Rule('Refolding', Proteins(b=None, Hbind=1, folding='miss') % HSP90(b=None, Hbind=1) + ATP() >>
            Proteins(b=None, Hbind=None, folding='good') + HSP90(b=None, Hbind=None) + ADP(), k5)
Parameter('k6', 6*10**-7)
Rule('Protein_degradation', Proteins(folding='miss') + ATP() >> ADP(), k6)
Parameter('k7', 10**-7)
Rule('Aggregation', Proteins(b=None, folding='miss') + Proteins(b=None, folding='miss') >> AggP(), k7)
Parameter('k8', 500)
Parameter('k9', 1)
Rule('HSP90_HSF1', HSP90(b=None, Hbind=None) + HSF1(b=None, b1=None, b2=None) |
                HSP90(b=1, Hbind=None) % HSF1(b=1, b1=None, b2=None), k8, k9)
Parameter('k10', 0.01)
Parameter('k12', 0.5)
Rule('Dimerize',
      HSF1(b1=None, b2=None) + HSF1(b1=None, b2=None) |
          HSF1(b1=None, b2=1) % HSF1(b1=None, b2=1),
      k10,
      k12)
Parameter('k11', 100)
Parameter('k13', 0.5)
Rule('Trimerize',
      HSF1(b1=None, b2=None) + HSF1(b1=None, b2=1) % HSF1(b1=None, b2=1) |
          HSF1(b1=2, b2=None) % HSF1(b1=2, b2=1) % HSF1(b1=None, b2=1),
      k11,
      k13)
Parameter('k14', 0.05)
Parameter('k15', 0.08)
Rule('DNA_binding', HSF1(b1=2, b2=None) % HSF1(b1=2, b2=1) % HSF1(b1=None, b2=1) + HSE(b1=None) |
            HSF1(b1=2, b2=None) % HSF1(b1=2, b2=1) % HSF1(b1=3, b2=1) % HSE(b1=3), k14, k15)
# Assuming the transcription factor get of DNA after transcription & None basal Expression
# Try 2 different ways see if there is any difference
Parameter('k16', 1000)
Rule('Transcription_Translation', HSF1(b1=2) % HSF1(b1=2, b2=1) % HSF1(b1=3, b2=1) % HSE(b1=3) >>
    HSF1(b=None, b1=None, b2=None) + HSF1(b=None, b1=None, b2=None) + HSF1(b=None, b1=None, b2=None)
    + HSE(b=None, b1=None) + HSP90(b=None, Hbind=None), k16)

Parameter('k17', 8.02*10**-9)
Rule('Degrades', HSP90(b=None, Hbind=None) + ATP() + ATP() >> ADP() + ADP(), k17)
# Only accounting the degradation of sHSP in mito
Parameter('k18', 12)
Rule('ATP_generation', ADP() >> ATP(), k18)
Parameter('k19', 0.02)
Rule('cellular_processes', ATP() >> ADP(), k19)
Parameter('k20', 0.01)
Rule('ROS_production', None >> ROS(), k20)
Parameter('k21', 0.001)
Rule('ROS_scavenged', ROS() >> None, k21)
