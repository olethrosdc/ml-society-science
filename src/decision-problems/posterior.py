

# Assume the number of models is equal to n=len(prior).  The argument
# P is an n-by-m array, where m is the number of possible
# predictions so that P[i][j] is the probability the i-th model assignsm to the j-th outcome. The outcome is a single number in 1, m.
import numpy as np
import random

## Calculate the posterior given a prior belief, a set of predictions, an outcome
## - prior: belief vector so that prior[i] is the probabiltiy of mdoel i being correct
## - P: P[i][j] is the probability the i-th model assignsm to the j-th outcome
## - outcome: actual outcome
def GetPosterior(prior, P, outcome):
    n_models = len(prior)
    posterior = prior # initialise the posterior
    ## So probability of outcome for model i is just...
        
    return posterior


## Get the probability of the specific outcome given your current
## - belief: vector so that belief[i] is the probabiltiy of mdoel i being correct
## - P: P[i][j] is the probability the i-th model assignsm to the j-th outcome
## - outcome: actual outcome
def GetMarginalPredictive(belief, P, outcome):
    n_models = len(belief)
    outcome_probability = 0 # initialise the probabiltiy
    
    ## average the outcome probability over all models
    
    return outcome_probability


T = 4
n_models = 3
prediction = np.zeros([n_models, T])

# build predictions. Replace this with the data in the example
prediction = np.matrix('0.1 0.2 0.3 0.4; 0.4 0.5 0.6 0.7; 0.7 0.8 0.9 0.99')


n_outcomes = 2 # 0 = no rain, 1 = rain

P = np.zeros([n_models, n_outcomes])
belief = np.ones(n_models) / n_models;
rain = [0, 1, 0, 0];


for t in range(T):
    for model in range(n_models):
        P[model,1] = prediction[model,t] # the table predictions give rain probabilities
        P[model,0] = 1.0 - prediction[model,t] # so no-rain probability is 1 - that.
    belief = GetPosterior(belief, P, rain[t])

                
    
