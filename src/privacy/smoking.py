import matplotlib.pyplot as plt
import numpy

## We want to calculate the share of people smoking
n_people = 100 # The number of people participating
epsilon = 0.1 # the amount of privacy we can lose

# Assume the probability of smoking is fixed
true_ratio = 0.1
data=numpy.zeros(n_people)
for i in range(n_people):
    data[i] = min(data[i], max_salary)

# Calculate the average salary
empirical_ratio = numpy.average(data)
print("The empirical ratio is ", empirical_ratio)

#### Random-Resposne mechanism for local DP
## If $\epsilon = ln (1-p)/p$ then we need to set $p = 1 / (1 + e^\epsilon)$
p_flip = 1 / (1 + numpy.exp(epsilon))
dp_data = numpy.zeros(n_people)
for i in range(n_people):
    if (numpy.random.binomial(
    dp_data[i] 
# Calculate the average
local_average = numpy.average(corrupted_data)
print("The average salary computed with local DP + Laplace is ", local_average)

#### Laplace mechanism for centralised DP
#
# We calculate the average, so if an individual's data changes by max_salary, the average
# changes by 1 / n. So:
central_sensitivity = 1 / n_people
# We now tune sensitivity to the function
central_noise = numpy.random.laplace(scale=central_sensitivity / epsilon, size=1)
# Calculate the average
central_average = numpy.average(data + central_noise)
print("The average salary computed with central DP + Laplace is ", central_average)


