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

def produceGraph(model, filename, methods, observe, parameters):
    # make a graph
    # parameters is list will run multiple times and put them on the same graph

    for name, monomer in observe.items():
        model.add_component(Observable(f'obs{name}', monomer))
    t = np.linspace(0, 100)
    fig, axs = plt.subplots(1, 1)

    for i, parameter_set in enumerate(parameters):
        for method in methods:
        # test without glutathionine and sHSP enabled
            simulationResult = BngSimulator(model).run(
                tspan=t,
                method=method,
                param_values=parameter_set
            )

            for name in simulationResult.observables.dtype.names:
                axs.plot(t, simulationResult.all[name], label=f'{method.upper()} {name} {i}')

    for i in range(0,1):
        axs.set_xlabel('Time in seconds')
        axs.set_ylabel('Number of molecules')
    # axs[0].set_ylim(ymin=0, ymax=10**7)
    axs.legend()
    # axs[1].legend()

    fig.savefig(f'export/{filename}.png')
