import numpy as np
import pandas

## In this example, we want to design a drug experiment
##
## Here, we have a number of drugs to try.


## The simulator generates the drugs and the outcomes
class Simulator:
    def __init__(self, n_drugs, n_features):
        self.n_drugs = n_drugs
        self.X = np.random.normal(size=[n_drugs, n_features])
        self.W = np.random.normal(size=n_features)
    def generate_outcome(self, action):
        y = self.X[action]@self.W
        return np.random.binomial(1, 1/(1 + np.exp(-y)))
    def evaluate_action(self, action, n_iter=10000):
        z = 0
        for t in range(n_iter):
            z += self.generate_outcome(action)
        return z / n_iter
    def best_action(self, n_iter=1000):
        v = np.zeros(self.n_drugs)
        for a in range(self.n_drugs):
            v[a] = self.evaluate_action(a)
        return [np.argmax(v), v]

## This is a policy for experimenting over drugs. Here it just randomly assigns drugs
class RandomPolicy:
    def __init__(self, drug_descriptions):
        self.n_actions = drug_descriptions.shape[0]
        self.counts = np.zeros(self.n_actions)
        self.outcomes = np.zeros(self.n_actions)
    def select_action(self):
        return np.random.choice(self.n_actions)
    def update(self, action, outcome):
        self.counts[action] += 1
        self.outcomes[action] += outcome
        return
    def best_action(self):
        z = self.outcomes / self.counts
        return np.argmax(z)
    def best_action_value(self):
        z = self.outcomes / self.counts
        return np.max(z)
    
if __name__ == '__main__':
    n_drugs = 8
    n_features = 4
    n_models = 16
    environment = Simulator(n_drugs, n_features)

    ## Get the drug descriptions and feed them to the policy
    policy = RandomPolicy(environment.X)
    T = 100
    for t in range(T):
        a_t = policy.select_action()
        y_t = environment.generate_outcome(a_t)
        policy.update(a_t, y_t)
    print ("Apparent best action: ", policy.best_action())
    print ("Apparent value:", policy.best_action_value())
    print ("Actual value:", environment.evaluate_action(policy.best_action()))
    [a_s, V] = environment.best_action()
    print("Best action:", a_s, "with value", V[a_s])
