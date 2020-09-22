import matplotlib.pyplot as plt
import numpy

## We want to calculate teh average salary
n_people = 100 # The number of people participating
max_salary = 10 # maximum salary of people - otherwise we can't use Laplace
epsilon = 0.1 # the amount of privacy we want to lose

# Assume the distribution of people is coming from a clipped gamma distribution. Not necessarily true
data = 

# Calculate the average salary

#### Laplace mechanism for local DP
#
# We need the sensitivity of individual data points. Since an
# individual's data can vary at most by max_salary, we have:
def LocalDP(data, epsilon, max_salary, n_people):
    return local_average

#### Laplace mechanism for centralised DP
#
# We calculate the average, so if an individual's data changes by max_salary, the average
# changes by max_salary / n. So:
def CentralDP(data, epsilon, max_salary, n_people):
    return central_average

## Generic loop to plot the variance
n_iter = 1000
variance_local = numpy.zeros(100)
variance_central = numpy.zeros(100)
t = 0
epsilon = numpy.linspace(0.1,1,100)
for t in range(100):
    central = numpy.zeros(n_iter)
    local = numpy.zeros(n_iter)
    for i in range(n_iter):
        central[i] = CentralDP(data, epsilon[t], max_salary, n_people)
        local[i] = LocalDP(data, epsilon[t], max_salary, n_people)
    variance_local[t] = numpy.var(local)
    variance_central[t] = numpy.var(central)

plt.plot(epsilon, variance_local)
plt.plot(epsilon, variance_central)
plt.legend("Local", "Central")
plt.show()
