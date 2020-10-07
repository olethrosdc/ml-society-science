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
                self.belief[1] += 1
            else:
                self.belief[0] += 1

    ## Get the marginal bernoulli probability of each symbol
    def get_marginal(self):
        return self.belief / sum(self.belief)

    ## Generate a bernoulli probability distribution from the posterior
    def generate(self):
        p = np.zeros(2)
        p[1] = np.random.beta(self.belief[0], self.belief[1])
        p[0] = 1 - p[1]
        return Bernoulli(p)

    ## Get the marginal probability for a large number of data.
    ## This has an analytical formula in this case.
    def likelihood(self, data):
        h = np.sum(data>0)
        n = len(data)
        return np.exp(betaln(self.belief[0] + h, self.belief[1]+n-h) - betaln(self.belief[0], self.belief[1]))

class Bernoulli:
    ## Initialise
    def __init__(self, p):
        self.p = p
        self.n_outcomes = len(p)

    ## This does nothing here
    def update_belief(self, data):
        return
    
    ## We define this to keep the same API, even though there is no marginal
    def get_marginal(self):
        return self.p

    ## Return the probability of a (sequence of) observations
    def predict_proba(self, x):
        return self.p[x]

    ## Generate n observations
    def generate(self, n):
        return np.random.choice(self.n_outcomes, n, p=self.p)

    def likelihood(self, data):
        h = np.sum(data>0)
        n = len(data)
        t = n - h;
        return pow(self.p[0], h) * pow(self.p[1], t)
