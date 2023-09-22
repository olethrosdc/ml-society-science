import k_anonymity

## This function takes a numpy 2D array as an input, and returns a
## k-anonymised array. 
def anonymise(D, k):

    X = D.copy()
    if (k_anonymity(X) < k):
        print("Fill this in")
    return X

import numpy as np
D = np.random.uniform(size=[16,2])
D_anon =anonymise(D)
print(k_anonymity(D))
print(k_anonymity(D_anon))


    
