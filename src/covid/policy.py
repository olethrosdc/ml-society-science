## A policy for treating individuals.
## 
##
## features: gender, age, income, genes, comorbidities, symptoms
## action: vaccines choice or treatment
## outcomes: symptoms (including covid-positive)

import numpy as np
from aux import symptom_names

class Policy:
    def __init__(self, n_actions, action_set):
        self.n_actions = n_actions
        self.action_set = action_set
        print("Initialising policy with ", n_actions, "actions")
        print("A = {", action_set, "}")
    ## Observe the features, treatments and outcomes of one or more individuals
    def observe(self, features, treatments, outcomes):
        pass
    ## Obtain the empirical utility of the policy on a set of one or more people
    def get_utility(self, features, treatment, outcome):
        return 0
    ## Get actions fro one or more people
    def get_action(self, features):
        return 0

## This is a purely random policy!
class RandomPolicy(Policy):
    ## Here the utiliy is defined in terms of the outcomes obtained only, ignoring both the treatment and the previous condition.
    def get_utility(self, features, treatment, outcome):
        actions = self.get_action(features)
        utility = 0
        utility -= 0.2 * sum(outcome[:,symptom_names['Covid-Positive']])
        utility -= 0.1 * sum(outcome[:,symptom_names['Taste']])
        utility -= 0.1 * sum(outcome[:,symptom_names['Fever']])
        utility -= 0.1 * sum(outcome[:,symptom_names['Headache']])
        utility -= 0.5 * sum(outcome[:,symptom_names['Pneumonia']])
        utility -= 0.2 * sum(outcome[:,symptom_names['Stomach']])
        utility -= 0.5 * sum(outcome[:,symptom_names['Myocarditis']])
        utility -= 1.0 * sum(outcome[:,symptom_names['Blood-Clots']])
        utility -= 100.0 * sum(outcome[:,symptom_names['Death']])
        return utility
    def get_action(self, features):
        if (features.ndim > 1):
            return np.random.choice(self.actions_set, features.shape[0])
        else:
            return np.random.choice(self.action_set)

    
