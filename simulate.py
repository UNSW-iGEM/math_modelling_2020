produceGraph(
    model,
    'temperature comparison',
    ['ode'],
    [{'NaturalProteins': Proteins(folding='good')}, {'ATP': ATP()}],
    [tempValues(-1), tempValues(0), tempValues(1), tempValues(2)]
)

# model = model.reload()
produceGraph(
    model,
    'no atp',
    ['ode'],
    [{'NaturalProteins': Proteins(folding='good')}, {'ATP': ATP()}],
    [{'ATP_0': 0}]
)
