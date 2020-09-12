from model import model

from pysb.simulator import ScipyOdeSimulator
import pylab

# time period
t = pylab.linspace(0, 1000)

simres = ScipyOdeSimulator(model, tspan=t).run()
yout = simres.all

pylab.ion()
pylab.figure()
pylab.plot(t, yout['NatP'], label="NatP")
pylab.plot(t, yout['MisP'], label="MisP")
pylab.plot(t, yout['MCom'], label="MisP/Hsp90 complex")
pylab.plot(t, yout['AggP'], label="AggP")
pylab.plot(t, yout['HSP90'], label="HSP90")
pylab.legend()
pylab.xlabel("Time (s)")
pylab.ylabel("Number of Molecules")
pylab.savefig('a.png')

pylab.ion()
pylab.figure()
pylab.plot(t, yout['ATP'], label="ATP")
pylab.plot(t, yout['ADP'], label="ADP")
pylab.plot(t, yout['ROS'], label="ROS")
pylab.legend()
pylab.xlabel("Time (s)")
pylab.ylabel("Number of Molecules")
pylab.savefig('b.png')
