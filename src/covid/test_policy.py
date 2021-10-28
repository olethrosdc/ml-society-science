## To-Do

import policy
import simulator


## Baseline simulator parameters
n_genes = 128
n_vaccines = 3
n_treatments = 4
n_population = 13

# symptom names for easy reference
from aux import symptom_names


# Create the underlying population
population = simulator.Population(n_genes, n_vaccines, n_treatments)
X = population.generate(n_population)

# Make sure that your policy appropriately filters out the population if necessary. This is just a random sample of 1000 people


# Generate vaccination results

print("Vaccination")
vaccine_policy = policy.RandomPolicy(n_vaccines, list(range(-1,n_vaccines))) # make sure to add -1 for 'no vaccine'

A = vaccine_policy.get_action(X)
Y = population.vaccinate(list(range(n_population)), A)
vaccine_policy.observe(X, A, Y)

# Generate treatment results
print("Treatment")
treatment_policy = policy.RandomPolicy(n_treatments, list(range(n_treatments)))

A = treatment_policy.get_action(X)
Y = population.treat(list(range(n_population)), A)
treatment_policy.observe(X, A, Y)


