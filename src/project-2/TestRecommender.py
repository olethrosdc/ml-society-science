import numpy as np
import pandas
def default_reward_function(action, outcome):
    return outcome

def test_policy(generator, policy, reward_function, T):
    policy.set_reward(reward_function)
    u = 0
    for t in range(T):
        x = generator.generate_features()
        a = policy.recommend(x)
        y = generator.generate_outcome(x, a)
        u += reward_function(a, y)
    return u

features = pandas.read_csv('data/medical/historical_X.dat', header=None, sep=" ").values
actions = pandas.read_csv('data/medical/historical_A.dat', header=None, sep=" ").values
outcome = pandas.read_csv('data/medical/historical_Y.dat', header=None, sep=" ").values
observations = features[:, :8]
labels = features[:,128] + features[:,129]*2

import reference_recommender
policy_factory = reference_recommender.ReferenceRecommender
policy = policy_factory()

import data_generation
generator = data_generation.DataGenerator()

## Fit the policy on historical data first
policy.fit_treatment_outcome(features, actions, outcome)

## Run an online test
n_tests = 1000
result = test_policy(generator, policy, default_reward_function, n_tests)
