from model import *
from util import produceGraph

produceGraph(
    model,
    'temperature comparison',
    ['ode'],
    [{'NaturalProteins': Proteins(folding='good')}, {'ATP': ATP()}],
    [tempValues(-1), tempValues(0), tempValues(1), tempValues(2)]
)

produceGraph(
    model,
    'no atp',
    ['ode'],
    [{'ATP': ATP()}],
    [{'ATP_0': 0}]
)
