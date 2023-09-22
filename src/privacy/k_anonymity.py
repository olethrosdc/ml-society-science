## Calculate whether a database satisfies k-anonymity
## Arugment: D, a database that has a len() equal to the number of people in it
def k_anonymity(D):
    n_subjects = len(D)
    min_equal = n_subjects
    ## go through each and every record and see how many records it is equal to
    for i in range(n_subjects):
        n_equal = 0
        for j in range(n_subjects):
            if (i!=j):
                if (D[i]==D[j]).all():
                    n_equal += 1
        min_equal = min(min_equal, n_equal)
    return min_equal

import numpy as np            
D = np.round(np.random.uniform(size=[8,2]))
print(D)            
print(k_anonymity(D))

