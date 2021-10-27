## To-Do

import policy
import simulator


## Baseline simulator parameters
n_genes = 128
n_vaccines = 3
n_treatments = 4

# symptom names for easy reference
from aux import symptom_names


# Create the underlying population
population = simulator.Population(n_genes, n_vaccines, n_treatments)
X = population.generate(10)

# Make sure that your policy appropriately filters out the population if necessary. This is just a random sample of 1000 people

print("OP");
# Generate vaccination results
v_set = list(range(-1,n_vaccines))
print(v_set)
vaccine_policy = policy.RandomPolicy(n_vaccines, list(range(-1,n_vaccines))) # make sure to add -1 for 'no vaccine'
print("X")
for t in range(X.shape[0]):
    a_t = vaccine_policy.get_action(X[t])
    y_t = population.vaccinate(t, a_t)
    vaccine_policy.observe(X[t], a_t, y_t)

# Generate treatment results
treatment_policy = policy.RandomPolicy(n_treatments, list(range(n_treatments)))
for t in range(X.shape[0]):
    a_t = treatment_policy.get_action(X[t])
    y_t = population.treat(t, a_t)
    treatment_policy.observe(X[t], a_t, y_t)


