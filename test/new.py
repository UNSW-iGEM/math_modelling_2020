from pysb import *
import matplotlib.pyplot as plt
import numpy as np

Model()

Monomer('A', ['b'])
Parameter('A_0', 2.0)

Initial(A(b=None), A_0)
Parameter('A_multiplier', 2.0)
Observable('A_total', A())
Expression('kf_A', A_total * A_multiplier)
Rule('bindA', A(b=None) + A(b=None) >> A(b=1) % A(b=1), kf_A)

# Monomer('ROS')

# Initial(ROS(), Parameter('t0_ROS', 1))
# Parameter('m', 2)
# Observable('ROS_total', ROS())
# Expression('k20', ROS_total * m)

# Rule('ROS_production', None >> ROS(), k20)

from pysb.simulator import ScipyOdeSimulator, KappaSimulator, BngSimulator

from pysb.export import export

# with open('model.kappa', 'w') as outfile:
#     outfile.write(export(model, 'kappa'))

sim = BngSimulator(model)
simres = sim.run(tspan=np.linspace(1, 1000), verbose=False, n_runs=1, method='ssa')

# simres = KappaSimulator(model, tspan = [0,1,2,3,4,5,6,7,8,9,10]).run()
# yout = simres.all

fig, axs = plt.subplots(3, 1)

axs[0].plot(t, yout['ROS_total'], label="ROS")
fig.savefig('a.png')
