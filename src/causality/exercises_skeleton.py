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
    
