from model import model

from pysb.simulator import ScipyOdeSimulator, BngSimulator
import pylab
import numpy as np

# time period
t = pylab.linspace(0, 10)

# simres = ScipyOdeSimulator(model, tspan=t).run()
# sim = StochKitSimulator(model, tspan=np.linspace(0, 10, 5))sim = BngSimulator(model)
sim = BngSimulator(model)
simres = sim.run(tspan=t, verbose=False, n_runs=1, method='ssa')
# simres = sim.run(n_runs=2, seed=123456)
yout = simres.all

pylab.ion()
pylab.figure()
pylab.plot(t, yout['NatP'], label="NatP")
pylab.plot(t, yout['MisP'], label="MisP")
pylab.plot(t, yout['obsMCom'], label="MisP/Hsp90 complex")
pylab.plot(t, yout['obsAggP'], label="AggP")
pylab.plot(t, yout['obsHSP90'], label="HSP90")
pylab.legend()
pylab.xlabel("Time (s)")
pylab.ylabel("Number of Molecules")
pylab.savefig('a.png')

pylab.ion()
pylab.figure()
pylab.plot(t, yout['obsATP'], label="ATP")
pylab.plot(t, yout['obsADP'], label="ADP")
pylab.plot(t, yout['obsROS'], label="ROS")
pylab.legend()
pylab.xlabel("Time (s)")
pylab.ylabel("Number of Molecules")
pylab.savefig('b.png')
