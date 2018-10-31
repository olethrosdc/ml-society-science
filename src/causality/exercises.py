## -*- Mode: python -*-
## Exercises for the lab

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class BasicPolicy:
    ## There is now one parameter for each possible value of x
    def __init__(self, pi):
        self.pi = pi
    def get_action(self, x=None):
        return int(np.random.choice(2, 1, p=[1-self.pi[x], self.pi[x]]))
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

class CovariateModel:
    ## Now the mean is a 2x2 matrix
    def __init__(self, mean):
        self.mean = mean
        #print("my mean: ", self.mean)
    def get_covariate(self):
        return int(np.random.choice(2, 1, p=[0.5, 0.5]))
    def get_response(self, data, action):
        #print("action: ", action, self.mean[action])
        return np.random.normal(self.mean[data, action], 1)

    
    

### Get an estimate for theta for the simple model where the response is an additive function (in expectation) of theta and the action



### Get an estimate for theta for the model where the response is one of two different normal distributions, whose mean arbitrarily depends on the action
theta = 0.1*np.random.normal(size=(2,2))
model = CovariateModel(theta)
policy = BasicPolicy(0.1)
n_samples = 10
n_actions = policy.get_n_actions()
a = np.empty(n_samples, dtype=int)
y = np.zeros(n_samples)
hat_theta = np.zeros(2)
hat_pi = np.zeros(2)
hat_U = 0
counts = np.zeros(2)
for t in range(n_samples):
    a[t] = int(policy.get_action())
    hat_pi[a[t]] +=1
    y[t] = model.get_response(a[t])
    counts[a[t]] += 1.0
    hat_theta[a[t]] += y[t]
    hat_U += y[t]

hat_pi /= sum(hat_pi)
hat_U/= n_samples
hat_theta /= counts
print("Parameters", theta)
print("Estimate parameters", hat_theta, "Policy:", hat_pi, "Utility:", hat_U)
#sns.distplot(y)
#plt.show()

## How do we estimate the utility of some other policy pi?

## Method 1: Use importance sampling
## E_P U = \sum_x U(x) P(x) = \sum_x U(x) P(x)/Q(x) Q(x)
## Approximated by  \sum_t U(x_t)P(x_t)/Q(x_t) x_t \sim Q

## This is how to estimate the utility of another policy using just the data.
alt_pi = np.zeros(n_actions)
alt_pi[np.argmax(hat_theta)] = 1
alt_hat_U = 0
for t in range(n_samples):
    alt_hat_U += y[t] * alt_pi[a[t]] / hat_pi[a[t]]

alt_hat_U /= n_samples
print("New policy: ", alt_pi)
print("Estimated Utility:", hat_U, alt_hat_U)

## This is how to estimate the utility of another policy using the estimated model parameters
U = 0
alt_U = 0
hat_U = 0
alt_hat_U = 0
for a in range(n_actions):
    hat_U += hat_pi[a] * hat_theta[a]
    alt_hat_U += alt_pi[a] * hat_theta[a]
    U += hat_pi[a] * theta[a]
    alt_U += alt_pi[a] * theta[a]

print("Estimated Utility:", hat_U, alt_hat_U)
print("True Utility:", U, alt_U)

