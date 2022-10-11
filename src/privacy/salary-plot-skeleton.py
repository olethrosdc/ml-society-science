import matplotlib.pyplot as plt
import numpy as np
import randomised_response
from laplace_mechanism import laplace_mechanism

## We want to calculate teh average salary
n_people = 1000 # The number of people participating
max_salary = 10 # maximum salary of people - otherwise we can't use Laplace
epsilon = 0.1 # the amount of privacy we want to lose

# Assume the distribution of people is coming from a clipped gamma
# distribution. Not necessarily true.  We are clipping the data to a
# maximum before seeing the data, so as to avoid inadvertedly
# revealing something about the data.
data = np.random.gamma(shape=2, scale=1, size=n_people)
for i in range(n_people):
    data[i] = min(data[i], max_salary)

# Calculate the average salary
average_salary = np.average(data)
print("The actual average salary is ", average_salary)





## Generic loop to plot the variance
n_iter = 1000
variance_local = np.zeros(100)
variance_central = np.zeros(100)
t = 0
epsilon = np.linspace(0.5,1,100)
for t in range(1):
    central = np.zeros(n_iter)
    local = np.zeros(n_iter)
    for i in range(n_iter):
        # calculate sensitivy, and set scale (lambda) according to that and epsilon
        central[i] = np.mean(data) + np.random.laplace(scale = 1) # fix the scale to the right value
    for i in range(n_iter):
        local[i] = np.mean(randomised_response.rp_float(data, epsilon[t], max_salary))
    plt.hist(central, alpha=0.5, bins=100)
    plt.hist(local, alpha=0.5, bins=100)
    plt.show()
    variance_local[t] = np.var(local)
    variance_central[t] = np.var(central)

plt.plot(epsilon, variance_local)
plt.plot(epsilon, variance_central)
plt.legend("Local", "Central")
plt.show()
