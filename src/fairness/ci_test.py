import numpy as np
from scipy.stats import beta
import matplotlib.pyplot as plt

## amount of data
n_data = 100000

## Firstly X is independent of all else
X = np.random.normal(size=n_data)
Y = np.zeros(n_data)
Z = np.zeros(n_data)
A = np.zeros(n_data)

for t in range(n_data):
    ## This is P(Z | X)
    Z[t] = X[t] + np.random.normal()
    if (Z[t] < 0):
        Z[t] = -1
    else:
        Z[t] = 1

    ## This is P(Y | X)
    Y[t] = X[t] + np.random.normal()
    if (Y[t] < 0):
        Y[t] = -1
    else:
        Y[t] = 1

    ## This is P(A | X)
    A[t] =  np.random.normal()
    if (A[t] < 0):
        A[t] = -1
    else:
        A[t] = 1


## Now measure the distribution of A for each value of Y, for different values of Z
##
n_figures = 0
for y in [-1, 1]:
    ## P(A | Y, Z = 1)
    positive = (Y==y) & (Z==1)
    positive_alpha = sum(A[positive]==1)
    positive_beta = sum(A[positive]==-1)
    positive_ratio = positive_alpha / (positive_alpha + positive_beta)

    ## P(A | Y, Z = - 1)
    negative = (Y==y) & (Z==-1)
    negative_alpha = sum(A[negative]==1)
    negative_beta = sum(A[negative]==-1)
    negative_ratio = negative_alpha / (negative_alpha + negative_beta)

    print("y: ", y, "Deviation: ", abs(positive_ratio - negative_ratio))

    print ("Now calculate a posterior distribution for the relevant Bernoulli parameter. Focus on just one value of y for simplicity")

    # First plot the joint distribution
    prior_alpha = 1
    prior_beta = 1
    xplot = np.linspace(0, 1, 200)
    pdf_p = beta.pdf(xplot, prior_alpha + positive_alpha, prior_beta + positive_beta)
    pdf_n = beta.pdf(xplot, prior_alpha + negative_alpha, prior_beta + negative_beta)
    pdf_m = beta.pdf(xplot, prior_alpha + positive_alpha + negative_alpha, prior_beta + positive_beta + negative_beta)
    n_figures+=1
    plt.figure(n_figures)
    plt.clf()
    plt.plot(xplot, pdf_p)
    plt.plot(xplot, pdf_n)
    plt.plot(xplot, pdf_m) 
    plt.legend(["z=1", "z=-1", "marginal"])
    plt.title("y=" + str(y))

plt.show()
