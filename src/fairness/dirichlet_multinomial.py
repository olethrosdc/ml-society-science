import numpy as np

class DirichletMultinomial:
    ## Initialise with an np.array of length N being the size of the alphabet
    def __init__(self, prior):
        self.belief = prior
        self.alphabet_size = len(prior)

    ## Get a list of observations in an array or list where data[t] is
    ## the symbol observed and update the posterior
    def update_belief(self, data):
        n_data = len(data)
        for t in range(n_data):
            belief[data[t]]+=1

    ## Get the marginal multinomial probability of each symbol
    def get_merginal(self):
        return belief / sum(belief)

    ## Generate a multinomial probability distribution from the posterior
    def generate(self):
        p = np.zeros(self.alphabet_size)
        for i in range(self.alphabet_size):
            p[i] = np.random.gamma(self.belief[i], 1)
        return Multinomial(p/sum(p))

class Multinomial:
    ## Initialise
    def __init__(self, p):
        self.p = p
        self.n_outcomes = len(p)
        
    ## Return the probability of a (sequence of) observations
    def predict_proba(self, x):
        return self.p[x]

    ## Generate n observations
    def generate(self, n):
        return np.random.choice(self.n_outcomes, n, p=self.p)
