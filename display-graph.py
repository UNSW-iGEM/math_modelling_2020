# make a graph without any text to display on the wiki

from pysb import *
from pysb.simulator import BngSimulator
import matplotlib.pyplot as plt
import numpy as np
from base_model import *


t = np.linspace(0, 100)
fig, axs = plt.subplots(1, 1)
model.add_component(Observable(f'obsATP', ATP()))
model.add_component(Observable(f'obsADP', ADP()))
simulationResult = BngSimulator(model).run(
    tspan=t,
    method='ssa',
    param_values={**tempValues(1), **{'ROS'}
)

for name in simulationResult.observables.dtype.names:
    axs.plot(t, simulationResult.all[name])

ax

fig.savefig(f'export/blank_graph.png')
