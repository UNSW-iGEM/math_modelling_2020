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
        'k2': [0.00002, 1],
        'k6': [6*10**-5, 1],
        'k7': [10**-7, 1],
        'k20': [1, 1],
        # 'k29': [10.0, 1],
        # 'k30': [10.0, 1],
    }
    return {key: value[0]*10**(magnitude*value[1]) for key, value in values.items()}

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
    fig, axs = plt.subplots(2, 2, constrained_layout=True, figsize=(10,6))
    fig.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=0.6, hspace=0.3)
    # fig.tight_layout(pad=5.0)

    # hack for when there is only one subplot
    if graphs == 1:
        axs = [axs]
    for i, parameter_set in enumerate(parameters):
        for method in methods:
        # test without glutathionine and sHSP enabled
            simulationResult = BngSimulator(model).run(
                tspan=t,
                method=method,
                param_values=parameter_set
            )
            for i, name in enumerate(simulationResult.observables.dtype.names):
                num = getGraph(observe, name)
                if (num == 0):
                    axs[0][0].plot(t, simulationResult.all[name], label=f'{method.upper()} {name} High Temp')
                elif (num == 1):
                    axs[0][1].plot(t, simulationResult.all[name], label=f'{method.upper()} {name} High Temp')
                elif (num == 2):
                    axs[1][0].plot(t, simulationResult.all[name], label=f'{method.upper()} {name} High Temp')
                else:
                    axs[1][1].plot(t, simulationResult.all[name], label=f'{method.upper()} {name} High Temp')
                

    for i in range(0, 2):
        for j in range(0,2):
            axs[i][j].set_xlabel('Time in seconds')
            axs[i][j].set_ylabel('Number of molecules')
            axs[i][j].legend()
            axs[i][j].set_ylim(bottom=0)
    axs[0][0].set_ylim(ymin=0, ymax=10**7)

    fig.savefig(f'export/{filename}.png')
