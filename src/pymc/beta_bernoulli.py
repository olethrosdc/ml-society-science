#https://docs.pymc.io/notebooks/getting_started.html

import pymc3 as mc
import numpy as np

basic_model = mc.Model()

data = np.array([0, 1, 0, 1])
import matplotlib.pyplot as plt

## Set up the model
with basic_model:
    data = np.array([1, 0, 0, 0, 1])
    theta = mc.Beta('theta', alpha=1, beta=1)
    y = mc.Bernoulli('y', p=theta, observed=data)

mc.model_to_graphviz(basic_model)

## Estimate distributions
with basic_model:
    start = mc.find_MAP() # Find starting value by optimization
    step = mc.NUTS(scaling=start) # Instantiate MCMC sampling algorithm
    trace = mc.sample(2000, step, start=start, njobs=4, progressbar=True)

## Plot
mc.traceplot(trace)
plt.show()
