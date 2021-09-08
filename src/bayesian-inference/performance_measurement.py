import numpy as np
## Two models, with different accuracies
accuracy = [0.6, 0.7]

def generate_uncorrelated_utils(n_examples, accuracy):
    n_models = len(accuracy) # finite number of models
    utils = np.zeros([n_examples, n_models]) # measure whether or not the models predict correctly
    
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
            if (0.5 * (X + np.random.uniform()) < accuracy[k]):
                utils[t,k] = 1
    return utils

n_examples = 10
correlated = generate_correlated_utils(n_examples, accuracy)
uncorrelated = generate_uncorrelated_utils(n_examples, accuracy)

print(np.mean(correlated[:,0] - correlated[:,1]))
print(np.mean(uncorrelated[:,0] - uncorrelated[:,1]))

alpha = 1
beta = 1


