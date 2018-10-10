# See https://docs.pymc.io/notebooks/getting_started.html for pymc documentation 

import pymc3 as mc
import numpy as np

model = mc.Model()

data = np.array([0, 1, 0, 1])
n_data = len(data)
n_outcomes = 5
n_movies = 10
import matplotlib.pyplot as plt

# setup model
model = mc.Model()
n_clusters = 3
with model:
    # clusters
    zeta = mc.Dirichlet('zeta', a=np.ones(n_clusters), shape=n_clusters)
    # latent cluster of each observation
    category = mc.Categorical('category',
                              p=zeta,
                              shape=n_data)
    theta = mc.Dirichlet('theta', a=np.ones(n_outcomes,n_movies), shape=n_clusters)
    
    # likelihood for each observed value
    y = mc.Bernoulli('y', p=theta[category], observed=data)

with model:
    step1 = mc.Metropolis(vars=[zeta, theta])
    step2 = mc.ElemwiseCategorical(vars=[category], values=[0, 1, 2])
    tr = mc.sample(10000, step=[step1, step2])


mc.traceplot(tr)
plt.show()

