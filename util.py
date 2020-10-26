from pysb import *
from pysb.simulator import BngSimulator
import matplotlib.pyplot as plt
import numpy as np

def tempValues(magnitude = 1):
    # varies temperature values by orders of magnitude
    # wiki writeup has justificatatin for these changes

    # first number is normal value, second number is whether they go up or not
    values = {
        'k1': [10, -1],
        'k6': [6*10**-7, 1],
        'k20': [0.1, 1],
        'k29': [10.0, 1],
        'k30': [10.0, 1],
    }
    return {key: value[0]*10**(magnitude*value[1]) for key, value in values.items()}

<<<<<<< HEAD
def getGraph(observe, name):
    for i, observes in enumerate(observe):
        for observableName in observes:
            if f'obs{observableName}' == name:
                return i

def produceGraph(model, filename, methods, observe, parameters):
    # make a graph
    # parameters is list will run multiple times and put them on the same graph
    model=model.reload()
    for graph in observe:
        for name, monomer in graph.items():
            model.add_component(Observable(f'obs{name}', monomer))
    t = np.linspace(0, 100)
    graphs = len(observe)
    fig, axs = plt.subplots(graphs, 1)
=======
def produceGraph(model, filename, methods, observe, parameters):
    # make a graph
    # parameters is list will run multiple times and put them on the same graph

    for name, monomer in observe.items():
        model.add_component(Observable(f'obs{name}', monomer))
    t = np.linspace(0, 100)
    fig, axs = plt.subplots(1, 1)

>>>>>>> 04f1bf7be56924dc48466956ecd9e44697b3b622
    for i, parameter_set in enumerate(parameters):
        for method in methods:
        # test without glutathionine and sHSP enabled
            simulationResult = BngSimulator(model).run(
                tspan=t,
                method=method,
                param_values=parameter_set
            )

            for name in simulationResult.observables.dtype.names:
<<<<<<< HEAD
                axs[getGraph(observe, name)].plot(t, simulationResult.all[name], label=f'{method.upper()} {name} {i}')

    for i in range(0, graphs):
        axs[i].set_xlabel('Time in seconds')
        axs[i].set_ylabel('Number of molecules')
        axs[i].legend()
        axs[i].set_ylim(bottom=0)
    # axs[0].set_ylim(ymin=0, ymax=10**7)
=======
                axs.plot(t, simulationResult.all[name], label=f'{method.upper()} {name} {i}')

    for i in range(0,1):
        axs.set_xlabel('Time in seconds')
        axs.set_ylabel('Number of molecules')
    # axs[0].set_ylim(ymin=0, ymax=10**7)
    axs.legend()
>>>>>>> 04f1bf7be56924dc48466956ecd9e44697b3b622
    # axs[1].legend()

    fig.savefig(f'export/{filename}.png')
