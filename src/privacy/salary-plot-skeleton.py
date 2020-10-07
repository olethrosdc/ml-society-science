import matplotlib.pyplot as plt
import numpy

## We want to calculate teh average salary
n_people = 100 # The number of people participating
max_salary = 10 # maximum salary of people - otherwise we can't use Laplace
epsilon = 0.1 # the amount of privacy we want to lose

# Assume the distribution of people is coming from a clipped gamma distribution. Not necessarily true
data = numpy.random.gamma(shape=2, scale=1, size=n_people)
for i in range(n_people):
    data[i] = min(data[i], max_salary)

# Calculate the average salary
average_salary = numpy.average(data)
print("The actual average salary is ", average_salary)


#### Laplace mechanism for local DP
#
# We need the sensitivity of individual data points. Since an
# individual's data can vary at most by max_salary, we have:
def LocalDPLaplace(data, epsilon, max_salary, n_people):
    noise = numpy.random.laplace(scale = max_salary/epsilon, size = n_people)
    local_average = numpy.average(data + noise)
    return local_average

#### Laplace mechanism for centralised DP
#
# We calculate the average, so if an individual's data changes by max_salary, the average
# changes by max_salary / n. So:
def CentralDPLaplace(data, epsilon, max_salary, n_people):
    sensitivity = max_salary / n_people
    noise = numpy.random.laplace(scale = sensitivity/epsilon, size = 1)
    central_average = numpy.average(data) + noise
    return central_average

#### Exponential mechanism for local DP
#
# Here each person uses the exponential mechanism to generate a
# response from their true data.
#
# The utility of different responses for a salary response
def LocalDPExponential(data, epsilon, max_salary, n_people):
    #utility = - abs(salary - response)^2?
    sensitivity = max_salary**2
    noise= numpy.random.normal(scale = sensitivity/epsilon, size = n_people)
    local_average = numpy.average(data + noise)
    return local_average


#### Exponential mechanism for central DP
#
# Here exponential mechanism to generate a
# response from their true data. 
def CentralDPExponential(data, epsilon, max_salary, n_people):
    sensitivity = (max_salary/n_people)**2  # not sure about this
    noise= numpy.random.normal(scale = sensitivity/epsilon, size = 1)
    local_average = numpy.average(data) + noise
    return central_average

### Exponential mechanism for local DP
#
# Here the exponential mechanism takes the utility as an input and a
# finite number of responses
def GenericExponentialMechanism(data, epsilon, utility, n_responses):
    L = utility.sensitivity()
    p = numpy.zeros(n_responses)
    for a in range(n_responses):
        p[a] = utility.calculate(answer, data)

    p /= p.sum()

    answer = numpy.random.choice(a = range(n_responses), p = p)
    
    return answer



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
        central[i] = CentralDPLaplace(data, epsilon[t], max_salary, n_people)
        local[i] = LocalDPLaplace(data, epsilon[t], max_salary, n_people)
    variance_local[t] = numpy.var(local)
    variance_central[t] = numpy.var(central)

plt.plot(epsilon, variance_local)
plt.plot(epsilon, variance_central)
plt.legend("Local", "Central")
plt.show()
