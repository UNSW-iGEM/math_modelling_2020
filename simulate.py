from model import *
from util import produceGraph

# produceGraph(
#     model,
#     'temperature comparison',
#     ['ode'],
#     [{'NaturalProteins': Proteins(folding='good')}, {'ATP': ATP()}],
#     [tempValues(-1), tempValues(0), tempValues(1), tempValues(2)]
# )

# produceGraph(
#     model,
#     'no atp',
#     ['ode'],
#     [{'ATP': ATP()}],
#     [{'ATP_0': 0}]
# )

# produceGraph(
#     model,
#     'Baseline model_0',
#     ['ssa'],
#     [{'NaturalProteins': Proteins(folding='good'),
#     'AggP': AggP()}, 
#     {'MisFoldProteins': Proteins(folding='miss')},
#     {'MisP_Hsp90': Proteins(b=None, Hbind=1, folding='miss') % HSP90(b=None, Hbind=1),
#     'ATP': ATP(),
#     'ADP': ADP()},
#     {'ROS': ROS()}],
#     [tempValues(0)]
# )
