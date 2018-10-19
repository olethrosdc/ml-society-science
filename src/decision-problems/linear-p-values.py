from __future__ import print_function
import numpy as np

n_data = 100000
n_features = 128
data = np.zeros([n_data, n_features ])
targets = np.zeros(n_data)
p = [ np.random.uniform() for i in range(n_features)]
q = np.random.uniform()

for t in range(n_data):
    for i in range(n_features):
        if (np.random.uniform() < p[i]):
            data[t,i] = 1
        else:
            data[t,i] = 0
    if (np.random.uniform() < q):
        targets[t] = 1
    else:
        targets[t] = 0

import pandas
data_in = pandas.DataFrame(data).add_prefix('X')
data_out = pandas.DataFrame(targets).add_prefix('Y')


# sklearn module
from sklearn.linear_model import LogisticRegression

## SM module
import statsmodels.api as sm
print ("Using statisticsmodels logit")
logit_model = sm.Logit(targets, data)
logit_res = logit_model.fit(method="bfgs") # for singularities
print(logit_res.summary())
print("The proportion of p-values which are smaller than p%")
for i in range(1,11):
    print(i, "%", np.mean(logit_res.pvalues<i/100))
    
#print ("Using the GLM interface for the same model")
#binomial_model = sm.GLM(targets, data, family=sm.families.Binomial())
#binomial_res = binomial_model.fit()
#print(binomial_res.summary())
#print(np.mean(binomial_res.pvalues<0.05))




