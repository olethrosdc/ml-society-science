import matplotlib.pyplot as plt
import numpy as np

## We want to calculate the share of people smoking
n_people = 100 # The number of people participating
epsilon = 0.1 # the amount of privacy we can lose

# Assume the probability of smoking is fixed
true_ratio = 0.1
data=np.random.coice(2, size=n_people, p=[1 - true_ratio, true_ratio])

# Calculate the average salary
empirical_ratio = np.average(data)
print("The empirical ratio is ", empirical_ratio)


import randomised_response

private_data = randomised_response.rp_binary(data, epsilon)

# Calculate the average
local_average = np.average(private_data)
print("The average probability of smoking computed with local DP + randomised response ", local_average)


