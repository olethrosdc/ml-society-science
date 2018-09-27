import numpy as np
from scipy.special import betaln
from scipy.stats import beta

class BetaBernoulli:
    ## Initialise with an np.array of length N being the size of the alphabet
    def __init__(self, prior):
        self.belief = prior

    ## Get a list of observations in an array or list where data[t] is
    ## the symbol observed and update the posterior. Symbols are either >0 or <= 0 for simplicity
    def update_belief(self, data):
        n_data = len(data)
        for t in range(n_data):
            if (data[t] > 0):
                belief[1] += 1
            else:
                belief[0] += 1

    ## Get the marginal bernoulli probability of each symbol
    def get_merginal(self):
        return belief / sum(belief)

    ## Generate a bernoulli probability distribution from the posterior
    def generate(self):
        p = np.zeros(self.alphabet_size)
        for i in range(self.alphabet_size):
            p[i] = np.random.gamma(self.belief[i], 1)
        return Bernoulli(p/sum(p))

    ## Get the marginal probability for a large number of data.
    ## This has an analytical formula in this case.
    def marginal_probability(self, data):
        h = np.sum(data>0)
        n = len(data)
        return np.exp(betaln(alpha + h, beta+n-h) - betaln(alpha, beta))

class Bernoulli:
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
