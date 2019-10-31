from exercises import *

import numpy as np

model = BasicModel(0.3)
policy = BasicPolicy(0.5)

n_data = 1000

a = np.zeros(n_data)
x = np.zeros(n_data)
for t in range(n_data):
    a[t] = policy.get_action()
    x[t] = model.get_response(a[t])
    

y = np.zeros(n_data)
for t in range(n_data):
    y[t] = x[t] - a[t]

print(np.mean(y))

### Get an estimate for theta for the model where the response is one of two different normal distributions, whose mean arbitrarily depends on the action
theta = 0.1*np.random.normal(size=2)
model = StandardModel(theta)
policy = BasicPolicy(0.1)
n_samples = 10
n_actions = policy.get_n_actions()
a = np.empty(n_samples, dtype=int)
y = np.zeros(n_samples)
hat_theta = np.zeros(2) # use this to estimate the model
hat_pi = np.zeros(2) # use this to estimate the policy
counts = np.zeros(2) # this is needed for getting the right 

## This corresponds to estimating the historical policy, the model parameters and the expected utility of that policy, with the only difference that the data here is generated online. So, the code could be used to estimate the utility of a new policy, if you had access to the model.
## Generate data
for t in range(n_samples):
    a[t] = int(policy.get_action()) 
    y[t] = model.get_response(a[t])
