import beta_bernoulli as bb
import numpy as np

## Prior over possible model hypotheses
model = []
model.append(bb.BetaBernoulli([1, 1]))
model.append(bb.Bernoulli([0.5, 0.5]))
prior = np.ones(2)/2 # uniform prior

## Generate data from the true model
p = 0.6
true_model = bb.Bernoulli([p, 1 - p])
n_data = 10
data = true_model.generate(n_data)

## Now do the standard Bayesian thing
likelihood = np.zeros(2)
for i in range(2):
    likelihood[i] = model[i].likelihood(data)

posterior = likelihood * prior
posterior /= sum(posterior)
print(posterior)





