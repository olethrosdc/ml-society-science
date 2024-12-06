import numpy as np
import pandas

## In this example, we want to design a drug experiment
##
## Here, we have a number of drugs to try.


## The simulator generates the drugs and the outcomes
class Simulator:
    def __init__(self, n_drugs):
        self.n_drugs = n_drugs
        self.mean = np.random.uniform(size=n_drugs)
    def step(self, action):
        return np.random.binomial(1, self.mean[action])
    def reset(self):
        pass

## This is a policy for experimenting over drugs. Here it just randomly assigns drugs
class RandomPolicy:
    def __init__(self, n_actions):
        self.n_actions = n_actions
    def reset(self):
        pass
    def act(self):
        return np.random.choice(self.n_actions)
    ## Here, we update what we learn from observing an action and a reward
    def update(self, action, reward):
        # step
        pass
    
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
