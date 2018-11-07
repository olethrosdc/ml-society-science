# -*- Mode: python -*-
# A simple reference recommender
#
#
# This is a medical scenario with historical data. 
#
# General functions
#
# - set_reward
# 
# There is a set of functions for dealing with historical data:
#
# - fit_data
# - fit_treatment_outcome
# - estimate_utiltiy
#
# There is a set of functions for online decision making
#
# - predict_proba
# - recommend
# - observe

from sklearn import linear_model
import numpy as np

class RandomRecommender:

    #################################
    # Initialise
    #

    def __init__(self):
        self.reward = self._default_reward

    ## By default, the reward is just equal to the outcome, as the actions play no role
    def _default_reward(self, action, outcome):
        return outcome

    # Set the reward function r(a, y)
    def set_reward(self, reward):
        self.reward = reward
    
    ##################################
    # Fit a model from patient data.
    #
    # This will generally speaking be an
    # unsupervised model. Anything from a Gaussian mixture model to a
    # neural network is a valid choice.  However, you can give special
    # meaning to different parts of the data, and use a supervised
    # model instead.
    def fit_data(self, data):
        print("Preprocessing data")
        return None


    ## Fit a model from patient data, actions and their effects
    ## Here we assume that the outcome is a direct function of data and actions
    def fit_treatment_outcome(self, data, actions, outcome):
        print("Fitting treatment outcomes")
        return None

    ## Estimate and return the utility of a specific policy from historical data.
    ## If the policy is None, return the utiltiy of the policy used on the observed data, i.e. the average utility obtained.
    ## If you are estimating confidence intervals or other statistics, you may print them out or use them internally, but do not return them.
    def estimate_utility(self, data, actions, outcome, policy=None):
        return 0

    # Return a distribution of effects for a given person's data and a specific treatment
    def predict_proba(self, data, treatment):
        return None
    
    # Return recommendations for a specific user data
    def recommend(self, user):
        print("Recommending")
        return None

    # Observe the effect of an action
    def observe(self, user, action, outcome):
        return None
