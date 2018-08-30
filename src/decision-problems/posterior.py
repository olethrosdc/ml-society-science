

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

    ## So probability of outcome for model i is just...
    return posterior


## Get the probability of the specific outcome given your current
## - belief: vector so that belief[i] is the probabiltiy of mdoel i being correct
## - P: P[i][j] is the probability the i-th model assignsm to the j-th outcome
## - outcome: actual outcome
def GetMarginalPredictive(belief, P, outcome):
    n_models = len(belief)
#...
    return outcome_probability

## In this function, U[action,outcome] should be the utility of the action/outcome pair
def GetExpectedUtility(belief, P, action, U):
    n_models = len(belief)
    n_outcomes = np.shape(P)[1]
    utility = 0
    for outcome in range(n_outcomes):
        p_outcome = GetMarginalPredictive(belief, P, outcome)
        utility += U[action, outcome] * p_outcome;
    return utility
    
def GetBestAction(belief, P, U):
    n_models = len(belief)
    n_actions = np.shape(U)[0]
...    
    return best_action
    

T = 4 # number of time steps
n_models = 3 # number of models

# build predictions for each station of rain probability
prediction = np.matrix('0.1 0.2 0.3 0.4; 0.4 0.5 0.6 0.7; 0.7 0.8 0.9 0.99')


n_outcomes = 2 # 0 = no rain, 1 = rain

## we use this matrix to fill in the predictions of stations
P = np.zeros([n_models, n_outcomes])
belief = np.ones(n_models) / n_models;
rain = [1, 0, 1, 1];


for t in range(T):
    # utility to loop to fill in predictions for that day
    for model in range(n_models):
        P[model,1] = prediction[model,t] # the table predictions give rain probabilities
        P[model,0] = 1.0 - prediction[model,t] # so no-rain probability is 1 - that.
    probability_of_rain = GetMarginalPredictive(belief, P, 1)
    print(probability_of_rain)
    U  = np.matrix('1 -1; 0 0')
    action = GetBestAction(belief, P, U)
    print(action, rain[t], U[action, rain[t]])
    belief = GetPosterior(belief, P, rain[t])
    print(belief)

                
    
