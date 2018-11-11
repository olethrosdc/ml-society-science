import numpy as np

class BernoulliBandit:
    def __init__(self, n_actions):
        self.n_actions = n_actions
        self.theta = np.random.beta(1, 1, size=self.n_actions)
        
    def generate(self, action):
        return 1 * (np.random.uniform() < self.theta[action])
