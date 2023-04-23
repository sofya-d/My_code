import numpy as np
import matplotlib.pyplot as plt
import random


# number of simulations
tries = 100000
observed_prob = 0.6
# size of experiment sample
sample_size = 100
# number of events we observed in our experiment
observed = sample_size * observed_prob
# probability of event based on previous observations
prob = 0.5
# expected number of events in our experiment sample based on probability of event got during previous observations
expected = sample_size * prob

# list of simulation results
sim_res = []

for _ in range(tries):
    # random() generates random number in range (0; 1), sample is list of bools indicating if random number is less than
    # probability of event based on previous observations
    sample = np.random.random(size = sample_size) <= prob
    # bool_sum is a number of "True" values in sample. It indicates how many random numbers are greater than probability of
    # event based on previous observations
    bool_sum = sum(sample)
    sim_res.append(bool_sum)


bins = np.arange(min(sim_res), max(sim_res), 1)
sample_size, bins, patches = plt.hist(sim_res, bins = bins)
# difference is a difference between observed and expected number of events
difference = abs(observed - expected)

for i, bin_ in enumerate(bins[:-1]):
    # if difference between simulation result and expected number of values is higher than difference between observed
    # and expected number of events bin will be colored red
    if abs(bin_ + prob - expected) >= difference:
        patches[i].set_facecolor('tomato')
plt.show()


cases = []
for res in sim_res:
    # if difference between simulation result and expected number of values is higher than difference between observed
    # and expected number of events is_more_dev = True
    is_more_dev = abs(res - expected) >= difference
    cases.append(is_more_dev)


# sum True values
true_cases = np.sum(cases)
print("p-value: ", true_cases / tries)
