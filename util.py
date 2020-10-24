from pysb.simulator import ScipyOdeSimulator, BngSimulator
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

def produceGraph(model, filename, methods, initials, parameters):
    t = np.linspace(0, 100)
    fig, axs = plt.subplots(1, 1)
    for trial, method in enumerate(methods):
    # test without glutathionine and sHSP enabled
        simulationResult = BngSimulator(model).run(
            tspan=t,
            verbose=False,
            # initials={Glutathione(state='reduced'): 0},
            method=method
        )

        for name in simulationResult.observables.dtype.names:
            data = simulationResult.all[name]
            # axis = 0 if data[0] > 10**3 else 1

            axs.plot(t, simulationResult.all[name], label=f'{method.upper()} {name}')

    for i in range(0,1):
        axs.set_xlabel('Time in seconds')
        axs.set_ylabel('Number of molecules')
    # axs[0].set_ylim(ymin=0, ymax=10**7)
    axs.legend()
    # axs[1].legend()

    fig.savefig(f'export/{filename}.png')
