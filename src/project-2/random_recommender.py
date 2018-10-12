# -*- Mode: python -*-
# A random recommender

class RandomRecommender:

    # Fit a model from patient data.
    # This will generally speaking be an
    # unsupervised model. Anything from a Gaussian mixture model to a
    # neural network is a valid choice.  However, you can give special
    # meaning to different parts of the data, and use a supervised
    # model instead.
    def fit_data(self, data):
        return None

    ## Fit a model from patient data, actions and their effects
    ## Patient data.
    def fit_treatment_outcome(self, data, actions, outcome):
        return None

    # Fit a model from historical data, given treatments, effects, as well as the treatment policy
    def fit_policy_outcome(self, data, actions, outcomes, policy):
        return None

    # Return a distribution of effects for a given person's data and a specific treatmentsssssssssssssssssssssssssssssss
    def predict_proba(self, data, treatment):
        return None
    
    # Return recommendations for a specific user data
    def recommend(self, user):
        return None

    # Observe the effect of an action
    def observe(self, user, action, reward):
        return None

