# -*- Mode: python -*-
# A random recommender

class RandomRecommender:

    # Fit a model from historical data
    # This will generally speaking be an unsupervised model. Anything from a Gaussian mixture model to a neural network is a valid choice.
    # However, you can give special meaning to different parts of the data. 
    def fit_data(self, data):
        return None

    # Fit a model from historical data, actions and their effects
    def fit_treatment_outcome(self, data, actions, outcome):
        return None

    # Fit a model from historical data, given treatments, effects, as well as the treatment policy
    def fit_policy_outcome(self, data, actions, outcomes, policy):
        return None

    # Return a distribution of effects 
    def predict_proba(self, genome, treatment):
        return None
    
    # Return recommendations for a specific user data
    def recommend(self, user):
        return None

    # Observe a the effect of an action
    def observe(self, user, action, reward):
        return None

