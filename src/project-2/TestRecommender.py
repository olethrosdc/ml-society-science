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
        r = reward_function(a, y)
        u += r
        policy.observe(x, a, y)
        print("x: ", x, "a: ", a, "y:", y, "r:", r)
    return u

features = pandas.read_csv('data/medical/historical_X.dat', header=None, sep=" ").values
actions = pandas.read_csv('data/medical/historical_A.dat', header=None, sep=" ").values
outcome = pandas.read_csv('data/medical/historical_Y.dat', header=None, sep=" ").values
observations = features[:, :8]
labels = features[:,128] + features[:,129]*2

import random_recommender
policy_factory = random_recommender.RandomRecommender
policy = policy_factory(2, 2)

import data_generation
generator = data_generation.DataGenerator()

## Fit the policy on historical data first
policy.fit_treatment_outcome(features, actions, outcome)

## Run an online test
n_tests = 10
result = test_policy(generator, policy, default_reward_function, n_tests)
print("Total reward:", result)
