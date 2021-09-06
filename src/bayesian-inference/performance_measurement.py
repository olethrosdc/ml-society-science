import numpy as np

accuracy = [0.6, 0.7]

def generate_uncorrelated_utils(n_examples, accuracy):
    n_models = len(accuracy)
    utils = np.zeros([n_examples, n_models])
    for t in range(n_examples):
        for k in range(n_models):
            if (np.random.uniform() < accuracy[k]):
                utils[t,k] = 1
    return utils

def generate_correlated_utils(n_examples, accuracy):
    n_models = len(accuracy)
    utils = np.zeros([n_examples, n_models])
    for t in range(n_examples):
        X = np.random.uniform()
        for k in range(n_models):
            if (X < accuracy[k]):
                utils[t,k] = 1
    return utils

n_examples = 100000
correlated = generate_correlated_utils(n_examples, accuracy)
uncorrelated = generate_uncorrelated_utils(n_examples, accuracy)

#for t in range(n_examples):
#    print(correlated[t], uncorrelated[t])

#print(correlated[:,0] - correlated[:,1])
#print(uncorrelated[:,0] - uncorrelated[:,1])

print(np.mean(correlated[:,0] - correlated[:,1]))
print(np.mean(uncorrelated[:,0] - uncorrelated[:,1]))
    

