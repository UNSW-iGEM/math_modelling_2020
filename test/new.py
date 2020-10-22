from pysb import *
import matplotlib.pyplot as plt
Model()

Monomer('ROS')

Initial(ROS(), Parameter('t0_ROS', 1))
Parameter('m', 2)
Observable('ROS_total', ROS())
Expression('k20', ROS_total * m)

Rule('ROS_production', None >> ROS(), k20)

from pysb.simulator import ScipyOdeSimulator, KappaSimulator

from pysb.export import export

with open('model.kappa', 'w') as outfile:
    outfile.write(export(model, 'kappa'))

simres = KappaSimulator(model, tspan = [0,1,2,3,4,5,6,7,8,9,10]).run()
yout = simres.all

fig, axs = plt.subplots(3, 1)

axs[0].plot(t, yout['ROS_total'], label="ROS")
fig.savefig('a.png')

