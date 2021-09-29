import matplotlib.pyplot as plt
import numpy as np
import randomised_response

## We want to calculate teh average salary
n_people = 100 # The number of people participating
max_salary = 10 # maximum salary of people - otherwise we can't use Laplace
epsilon = 0.1 # the amount of privacy we want to lose

# Assume the distribution of people is coming from a clipped gamma distribution. Not necessarily true
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
epsilon = np.linspace(0.1,1,100)
for t in range(100):
    central = np.zeros(n_iter)
    local = np.zeros(n_iter)
    for i in range(n_iter):
        central[i] = CentralDPLaplace(data, epsilon[t], max_salary, n_people)
        local[i] = LocalDPLaplace(data, epsilon[t], max_salary, n_people)
    variance_local[t] = np.var(local)
    variance_central[t] = np.var(central)

plt.plot(epsilon, variance_local)
plt.plot(epsilon, variance_central)
plt.legend("Local", "Central")
plt.show()
