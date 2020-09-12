from model import model

from pysb.simulator import ScipyOdeSimulator
import pylab

# time period
t = pylab.linspace(0, 1000)

simres = ScipyOdeSimulator(model, tspan=t).run()
yout = simres.all
pylab.ion()
pylab.figure()
pylab.plot(t, yout['NatP'], label="natP")
# pylab.plot(t, yout['obstBid'], label="tBid")
# pylab.plot(t, yout['obsC8'], label="C8")
pylab.legend()
pylab.xlabel("Time (s)")
pylab.ylabel("Molecules/cell")
pylab.savefig('out.png')
