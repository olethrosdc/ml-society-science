import numpy as np
import pandas

class Model:
    ## Just fit Beta-Bernoulli models
    def fit(self, data):
        self.alpha = np.ones(2)
        self.beta = np.ones(2)
        n_data = data.shape[0]
        for t in range(n_data):
            smoking = data[t,0]
            self.alpha[smoking] += data[t,1]
            self.beta[smoking] += 1 - data[t,1]
        return None
    
    def Evaluate(self):
        ## For example calculate the KL divergence between the prior for alpha=beta=1, the current posterior and return it. Maximising this, maximises our information about the relationship between smoking and cancer
        ## As a stupid example, just use this divergence, which however ignores the uncertainty
        return np.abs(self.alpha[0]/(self.alpha[0] + self.beta[0]) - self.alpha[1]/(self.alpha[1] + self.beta[1]))

class Policy:
    ## Should be a vector
    def __init__(self, ratio):
        self.ratio = ratio
        #print("ratio:", ratio)
    def select_action(self, n_data=1):
        return np.random.choice(2, p=self.ratio, size=n_data)

## Here, the generator is randomly created, so that when we run an experiment, we get a random result, but the thing is that our policy should be behaving well on average, no matter how the actual data is generated. In some sense, the generator is a programmatic description of a prior
class DataGenerator:
    def __init__(self):
        self.p = np.random.uniform(size=2) # 0 indicates no smoking, 1 smoking
        self.p[0]/=2 # here just encode that non-smokers probably have less cancer
        #print("P:", self.p)
    def generate_outcome(self, A):
        Y = 1*(np.random.uniform(size=A.shape) < self.p[A])
        return Y

    def generate_data(self, n_data, policy):
        actions = policy.select_action(n_data)
        cancer = self.generate_outcome(actions)
        return pandas.DataFrame({'smoking': actions, 'cancer': cancer})


def Evaluate(n_data=100, p=[0.5, 0.5]):
    policy = Policy(p)
    generator = DataGenerator()
    data = generator.generate_data(n_data, policy)
    model = Model()
    model.fit(data.values)
    information_gain = model.Evaluate()
    negative_impact = sum(data['cancer'])
    return - 0.0001*negative_impact + information_gain

if __name__ == '__main__':
    for n in [1, 10, 100, 1000, 10000]:
        for a in [0.1, 0.25, 0.5, 0.75, 0.9]:
            U = 0
            for t in range(1000):
                U += Evaluate(n, p=[a, 1-a])
            print("n: ", n, "a:", a, "U:", U/1000)



        
    

