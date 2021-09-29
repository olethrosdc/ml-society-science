import matplotlib.pyplot as plt
import numpy as np

## We want to calculate the share of people smoking
## Repeat the experiment for varying people and epsilon
n_people = 1000 # The number of people participating
epsilon = 1 # the amount of privacy we can lose

# Assume the probability of smoking is fixed.
true_ratio = 0.1
# Now we generate some data.
data=np.random.choice(2, size=n_people, p=[1 - true_ratio, true_ratio])

# Calculate the average salary
empirical_ratio = np.average(data)
print("The empirical ratio is ", empirical_ratio)



import randomised_response

# Implement the randomised response mechanism
# so that the flipping probability gives you exactly
# epsilon differential privacy
private_data = randomised_response.rp_binary(data, epsilon)

# Calculate the average on the private version of the data
local_average = np.average(private_data)
print("The average probability of smoking computed with local DP + randomised response ", local_average)


