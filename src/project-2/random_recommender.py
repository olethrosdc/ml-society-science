# -*- Mode: python -*-
# A random recommender

class RandomRecommender:

    # Fit a model to data from historical ratings
    def fit_ratings(self, ratings):
        return None

    # Fit a model to data from historical clicks, given a policy
    def fit_clicks(self, clicks, policy):
        return None

    # Return a distribution rating probabilities
    def predict_proba(self, user, item):
        return None
    
    # Return recommendations for a specific user data
    def recommend(self, user):
        return None

    # Observe a the effect of an action
    def observe(self, user, action, reward):
        return None

