import matplotlib.pyplot as plt
import numpy as np
import randomised_response
from laplace_mechanism import laplace_mechanism

## We want to calculate teh average salary
n_people = 10000 # The number of people participating
max_salary = 10 # maximum salary of people - otherwise we can't use Laplace
epsilon = 0.1 # the amount of privacy we want to lose

# Assume the distribution of people is coming from a clipped gamma
# distribution. Not necessarily true.  We are clipping the data to a
# maximum before seeing the data, so as to avoid inadvertedly
# revealing something about the data.
data = np.random.gamma(shape=2, scale=1, size=[n_people,1]) # shape is [n,1] to make sure that the second dimension is defined
for i in range(n_people):
    data[i] = min(data[i], max_salary)

# Calculate the average salary
average_salary = np.average(data)
print("The actual average salary is ", average_salary)





## Generic loop to plot the variance
n_iter = 10

t = 0
sensitivity = max_salary / n_people
n_epsilons = 10
epsilon = np.linspace(0.01,1,n_epsilons)
variance_local = np.zeros(n_epsilons) - 10
variance_central = np.zeros(n_epsilons) - 10
for t in range(n_epsilons):
    central = np.zeros(n_iter)
    local = np.zeros(n_iter)
    for i in range(n_iter):
        # calculate sensitivy, and set scale (lambda) according to that and epsilon
        # scale should be L/epsilon
        central[i] = np.mean(data)
    for i in range(n_iter):
        local[i] = np.mean(randomised_response.rp_float(data, epsilon[t], 1)
    print(central)
    print(local)
    print(sensitivity)
    #plt.hist(local, alpha=0.5)
    #plt.hist(central, alpha=0.5)
    #plt.legend(["Local", "Central"])
    #plt.title(epsilon[t])
    #plt.show()
    variance_local[t] = np.var(local)
    variance_central[t] = np.var(central)

plt.loglog(epsilon, variance_local)
plt.loglog(epsilon, variance_central)
plt.legend("Local", "Central")
plt.show()
