import numpy as np
import random
import scipy.stats
from collections import Counter


# #### Observed frequencies
# number of simulations
tries = 10000
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

print(sim_res[:10])


val_freq = Counter(sim_res)
val_freq = dict(val_freq)
prob_sum = 0
for val in val_freq.values():
    prob_sum += val / tries

print(f"Minimal value is {min(sim_res)} and probability sum is {prob_sum}, shi squared test is applicable")


# #### Expected frequencies


binom_dist = list(scipy.stats.binom.rvs(n=100, p=0.5, size=tries))
print(binom_dist[:10])


val_freq = Counter(binom_dist)
val_freq = dict(val_freq)
prob_sum = 0
for val in val_freq.values():
    prob_sum += val / tries

print(f"Minimal value is {min(sim_res)} and probability sum is {prob_sum}, shi squared test is applicable")


scipy.stats.chisquare(sim_res, binom_dist)


sample_size = 100
success_prob = 0.5
success_num_obs = 60


# ### Hypothesis testing with theory


dist = scipy.stats.binom(sample_size, success_prob)
print("p-value:", dist.cdf(sample_size - success_num_obs) + dist.sf(success_num_obs - 1))


# ### Hypothesis testing with build-in tests


print("p-value:", scipy.stats.binom_test(success_num_obs, sample_size, success_prob))


sample_size = 200
success_prob = 0.25
success_num_obs = 62


# ### Hypothesis testing with theory


dist = scipy.stats.binom(sample_size, success_prob)
mean = dist.mean()
dev = success_num_obs - mean
print("p-value:", dist.cdf(mean - dev) + dist.sf(success_num_obs - 1))


# ### Hypothesis testing with build-in tests


print("p-value", scipy.stats.binom_test(success_num_obs, sample_size, success_prob))


# ### Preparation for hypothesis testing
success_prob = 0.7
success_prob_obs = 0.73


# ### Hypothesis testing with theory
p_value = 1
sample_size = 0
while p_value >= 0.05:
    sample_size += 1
    dist = scipy.stats.binom(sample_size, success_prob)
    success_num_obs = success_prob_obs * sample_size
    mean = dist.mean()
    dev = success_num_obs - mean
    p_value = dist.cdf(mean - dev) + dist.sf(success_num_obs - 1)

print("Sample size:", sample_size)


import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

p_values = []
for sample_size in range(900, 1001, 10):
    dist = scipy.stats.binom(sample_size, success_prob)
    success_num_obs = success_prob_obs * sample_size
    mean = dist.mean()
    dev = success_num_obs - mean
    p_value = dist.cdf(mean - dev) + dist.sf(success_num_obs - 1)
    p_values.append(p_value)

plt.scatter(range(900, 1001, 10), p_values)
plt.xticks(np.arange(500, 1001, 10))
plt.plot([900, 1001], [0.05, 0.05], color='red')


# #### p-values seem to steadily lay under 0.05 when sample size becomes equal or bigger then 940.

# ### Hypothesis testing with build-in tests


p_value = 1
sample_size = 0
while p_value >= 0.05:
    sample_size += 1
    success_num_obs = success_prob_obs * sample_size
    p_value = scipy.stats.binom_test(success_num_obs, sample_size, success_prob)

print("Sample size:", sample_size)


p_values = []
for sample_size in range(900, 1001, 10):
    success_num_obs = success_prob_obs * sample_size
    p_value = scipy.stats.binom_test(success_num_obs, sample_size, success_prob)
    p_values.append(p_value)

plt.scatter(range(900, 1001, 10), p_values)
plt.xticks(np.arange(500, 1001, 10))
plt.plot([900, 1001], [0.05, 0.05], color='red')


# #### p-values seem to steadily lay under 0.05 when sample size becomes equal or bigger then 940.
# ### Check if errors have Poisson distribution


import numpy as np
from collections import Counter
import random
import scipy.stats


import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [7, 3]
plt.rcParams['figure.dpi'] = 100


# #### Observed frequencies


def simulate_seq(seq_len):
    seq = []
    for _ in range(seq_len):
        num = np.random.random(size = 1)
        if 0 <= num <= 0.15:
            nuc = "A"
        elif 0.15 < num <= 0.5:
            nuc = "C"
        elif 0.5 < num <= 0.85:
            nuc = "G"
        else:
            nuc = "T"
        seq.append(nuc)
    return "".join(seq)


def error_func(exprected, observed):
    return (exprected - observed) ** 2 / exprected


sim_num = 10_000
seq_len = 400
sim_seqs = []
nucleotides = ['A', 'C', 'G', 'T']
errors = []

for _ in range(sim_num):
    seq = simulate_seq(seq_len)
    observed_freqs = Counter(seq)
    error = 0

    for nucleotide in nucleotides:
        if nucleotide in "GC":
            expected = seq_len * 0.35
        else:
            expected = seq_len * 0.15
        
        observed = observed_freqs[nucleotide]
        error += error_func(expected, observed)
    
    errors.append(error)


bins = np.arange(min(errors), round(max(errors) + 1, 0), 1)
counts, bins, bars = plt.hist(errors, bins=bins)

plt.show()


print("bins:", bins, "\n")
print("len(bins):", len(bins), "\n")
print("counts:", counts, "\n")
print("len(counts):", len(counts))


obs_freqs = [int(num) for num in counts]
print("Observed frequancies:", obs_freqs)
print("len(obs_freqs):", len(obs_freqs))


print("OK frequencies:", obs_freqs[:15])
print("Too small frequencies:", obs_freqs[15:])
print("Value in merged bin:", sum(obs_freqs[15:]))
obs_freqs_merged = obs_freqs[:15] + [sum(obs_freqs[15:])]
print("Observed frequencies with merged bins:", obs_freqs_merged)
print("len(obs_freqs_merged):", len(obs_freqs_merged))


# #### Expected frequencies
dist = scipy.stats.chi2(3)
probs = dist.pdf(list(range(1, 30)))
print(probs)
print("len(probs):", len(probs))


exp_freqs = list(10_000 * probs)
print(exp_freqs)
print(len(exp_freqs))


print("OK frequencies:", exp_freqs[:15])
print("Too small frequencies:", exp_freqs[15:])
print("Value in merged bin:", sum(exp_freqs[15:]))
exp_freqs_merged = exp_freqs[:15] + [sum(exp_freqs[15:])]
print("Expected frequencies with merged bins:", exp_freqs_merged)
print("len(exp_freqs_merged):", len(exp_freqs_merged))


scipy.stats.chisquare(obs_freqs_merged, exp_freqs_merged)


def error_func(exprected, observed):
    return (exprected - observed) ** 2 / exprected

seq_len = 400
observed = [48, 164, 129, 59]
expected = [seq_len * prob for prob in [0.15, 0.35, 0.35, 0.15]]

error = 0
for i in range(len(observed)):
    obs = observed[i]
    exp = expected[i]
    error += error_func(exp, obs)

print("Error:", error)


# ### Hipothesis testing with theory


dist = scipy.stats.chi2(3)
p_value = dist.sf(error)
print("p-value:", p_value)


# ### Hipothesis testing with build-in tests


scipy.stats.chisquare(observed, expected)


expected = np.array([[573.8898, 291.64410000000004, 904.0086000000001, 1167.4575], [1380.1102, 701.3559, 2173.9914000000003, 2807.5425000000005]])
observed = np.array([[585, 284, 907, 1161], [1369, 709, 2171, 2814]])
observed_error = ((expected - observed) ** 2 / expected).sum()

print(f'Error of given data sample: {observed_error}')


# ### Hypothesis testing with theory


row_num, col_num = expected.shape
k = (col_num - 1) * (row_num - 1)
print("Number of rows:", row_num)
print("Number of columns:", col_num)
print("Degrees of freedome:", k)


dist = scipy.stats.chi2(3)
p_value = dist.sf(observed_error)
print("p-value:", p_value)


# ### Hypothesis testing with build-in tests


p_value = scipy.stats.chisquare(observed[0], expected[0])
print("For 'ill' category:", p_value)

p_value = scipy.stats.chisquare(observed[1], expected[1])
print("For 'healthy' category:", p_value)
