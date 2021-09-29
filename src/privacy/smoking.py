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


import randomised_response

private_data = randomised_response.rp_binary(data, epsilon)

# Calculate the average
local_average = numpy.average(private_data)
print("The average salary computed with local DP + randomised response ", local_average)

central_average = numpy.average(data + central_noise)
print("The average salary computed with central DP + Laplace is ", central_average)


