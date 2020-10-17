from model import model

from pysb.simulator import ScipyOdeSimulator, BngSimulator
import numpy as np
import matplotlib.pyplot as plt

# time period
t = np.linspace(0, 10)

# simres = ScipyOdeSimulator(model, tspan=t).run()
# sim = StochKitSimulator(model, tspan=np.linspace(0, 10, 5))sim = BngSimulator(model)
sim = BngSimulator(model)
simres = sim.run(tspan=t, verbose=False, n_runs=1, method='ssa')
# simres = sim.run(n_runs=2, seed=123456)
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


fig.savefig('a.png')
