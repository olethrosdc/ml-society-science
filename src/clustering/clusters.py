# Clusters
#
#
#
# Generate data
#

import numpy as np

n_clusters = 2
n_test_clusters = 2
# get a multinomial distribution parameter vector over the clusters
p_cluster = np.random.dirichlet(np.ones(n_clusters))
n_outcomes = 4
# get a bunch of Bernoulli parameters
theta = np.random.beta(1, 1, size=[n_clusters, n_outcomes])

n_data = 10000
X = np.zeros([n_data, n_outcomes])
for t in range(n_data):
    c = np.random.choice(n_clusters, p = p_cluster)
    X[t] = np.random.binomial(1, p = theta[c])


def fit_bernoulli_means(X, density, n_clusters, n_iter):
    n_data = X.shape[0]
    n_outcomes = X.shape[1]
    # get a bunch of Bernoulli parameters
    theta = np.random.beta(1, 1, size=[n_clusters, n_outcomes])
    prior = np.ones(n_clusters) / n_clusters
    p = np.zeros(n_clusters)
    for iter in range(n_iter):
        new_theta = np.zeros([n_clusters, n_outcomes])
        counts = np.zeros(n_clusters)
        for t in range(n_data):
            # get p(c | x_t, theta)
            for c in range(n_clusters):
                p[c] = density(X[t], theta[c])
            p = p/p.sum()
            # add the new point to the cluster center
            # E(theta | c, x_t)
            for c in range(n_clusters):
                new_theta[c] += X[t] * p[c]
                counts[c] += p[c]
        for c in range(n_clusters):
            theta[c] = new_theta[c]/counts[c]
    return theta

def bernoulli_density(x, theta):
    p = 1;
    #print(x, theta)
    for i in range(len(x)):
        assert (theta[i] >= 0 and theta[i] <=1)
        if (x[i]>0):
            p *= (theta[i])
        else:
            p *= (1 - theta[i])
    return p

theta_hat = fit_bernoulli_means(X, bernoulli_density, n_test_clusters, 100);
print(np.ceil(100*theta))
print(np.ceil(100*theta_hat))


            
