## -*- Mode: python -*-
## Exercises for the lab

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class BasicPolicy:
    def __init__(self, pi):
        self.pi = pi
    def get_action(self):
        return np.random.choice(2, 1, p=[1-self.pi, self.pi])
    def get_n_actions(self):
        return 2

class MarkovPolicy:
    ## There is now one parameter for each possible value of x
    def __init__(self, pi):
        self.pi = pi
    def get_action(self, x):
        p = self.pi[x]
        return np.random.choice(2, 1, p=[1-p, p])
    def get_n_actions(self):
        return 2

    
class BasicModel:
    def __init__(self, mean):
        self.mean = mean
    def get_response(self, action):
        return np.random.normal(action + self.mean, 1)

class StandardModel:
    ## Now the mean is a vector
    def __init__(self, mean):
        self.mean = mean
        #print("my mean: ", self.mean)
    def get_response(self, action):
        #print("action: ", action, self.mean[action])
        return np.random.normal(self.mean[action], 1)
    def Evaluate(self, policy, n_samples):
        hat_U = 0
        for t in range(n_samples):
            a = policy.get_action()
            y = self.get_response(a)
            hat_U += y
        return hat_U/n_samples
    
class CovariateModel:
    ## Now the mean is a 2x2 matrix
    def __init__(self, mean):
        self.mean = mean
    def get_covariate(self):
        return np.random.choice(2, 1, p=[0.5, 0.5])
    def get_response(self, covariate, action):
        return np.random.normal(self.mean[covariate, action], 1)
    def Evaluate(self, policy, n_samples):
        hat_U = 0
        for t in range(n_samples):
            x = self.get_covariate()
            a = policy.get_action(x)
            y = self.get_response(x, a)
            hat_U += y
        return hat_U/n_samples



