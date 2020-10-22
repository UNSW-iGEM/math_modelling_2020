from model import model

from pysb.simulator import ScipyOdeSimulator
import numpy as np
import matplotlib.pyplot as plt

simulator = ScipyOdeSimulator(model)

t = np.linspace(0, 1000)

results = simulator.run(tspan=t, param_values={'NatP': 0})
