import numpy as np

## The expected utility for a fixed action and a random outcome
##
## In this setting, the outcome does not depend on the action
##
## utility: NxK matrix
## action: in range(N)
## outcome_probabilities: vector of probabilities for K outcomes
def expected_utility_independent_outcome(utility, action, outcome_probabilities):
    return EU
    
## The expected utility for a fixed action and a random outcome
##
## In this setting, the outcome depends on the action
##
## utility: NxK matrix
## action: in range(N)
## outcome_probabilities: NxK matrix outcomes so that outcome_probabilities[action][outcome] gives the probability of an outcome given the action
def expected_utility_joint_action_outcome(utility, action, outcome_probabilities_given_action):
    return EU

## Gets f as a n input
def get_max_action(utility, prob, f):
    n_actions = utility.shape[0]
    U = np.zeros(n_actions)
    ## ... fill
    return np.argmax(U)

## Get the expected utility for the case of independent outcomes
utility = np.array(np.mat('-1 0 1; 10 0 -10'))
outcome_probabilities = np.array([0.5, 0.3, 0.2])
print(expected_utility_independent_outcome(utility, 1, outcome_probabilities))

## get the optimal action
print(get_max_action(utility,
                     outcome_probabilities,
                     expected_utility_independent_outcome))


## Get the expected utility for the case of dependent outcomes
outcome_probabilities_given_action = np.array(np.mat('0.1 0.2 0.7; 0.5 0.4 0.1'))
print(expected_utility_joint_action_outcome(utility, 1, outcome_probabilities_given_action))

## get the optimal action
print(get_max_action(utility,
                     outcome_probabilities_given_action,
                     expected_utility_joint_action_outcome))

