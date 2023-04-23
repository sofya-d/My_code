# ## HW4, Task2

# ### $H_0$ — mutation of base 12346 in 15th chromosome and SGD are independent.
# ### $H_1$ — mutation of base 12346 in 15th chromosome and SGD are dependent.
# ### p-value threshold = 0.05.

# #### Set-up


import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

plt.rcParams['figure.figsize'] = [9, 4]
plt.rcParams['figure.dpi'] = 100


# #### The first element of the list corresponds to number of nucleotide in healthy individuals, the second element of the list corresponds to number of nucleotide in ill individuals.

nuc_num = {"A": [0, 0], "C": [0, 0], "G": [0, 0], "T": [0, 0]}


with open("onesnp.csv") as snps:
    lines = snps.readlines()
    
for line in lines[1:len(lines)]:
    row = line.rstrip().split(",")
    nuc = row[0]
    status = int(row[1])
    
    if status == 0: # healthy
        nuc_num[nuc][0] += 1
    else: # ill
        nuc_num[nuc][1] += 1

print(nuc_num)


ind_num = len(lines) - 1

healthy_num = 0
ill_num = 0
for nums in nuc_num.values():
    healthy_num += nums[0]
    ill_num += nums[1]

ill_prob = ill_num / ind_num
healthy_prob = healthy_num / ind_num

print(f'P(ill): {ill_prob}')
print(f'P(healthy): {healthy_prob}')


# #### Probabilities for independent case


# P(specific nucleotide) * P(ill)
A_prob = sum(nuc_num["A"]) / ind_num
C_prob = sum(nuc_num["C"]) / ind_num
G_prob = sum(nuc_num["G"]) / ind_num
T_prob = sum(nuc_num["T"]) / ind_num

A_ill = A_prob * ill_prob
C_ill = C_prob * ill_prob
G_ill = G_prob * ill_prob
T_ill = T_prob * ill_prob

A_healthy = (sum(nuc_num["A"]) / ind_num) * healthy_prob
C_healthy = (sum(nuc_num["C"]) / ind_num) * healthy_prob
G_healthy = (sum(nuc_num["G"]) / ind_num) * healthy_prob
T_healthy = (sum(nuc_num["T"]) / ind_num) * healthy_prob

print(f'P(ill & A): {A_ill}')
print(f'P(ill & C): {C_ill}')
print(f'P(ill & G): {G_ill}')
print(f'P(ill & T): {T_ill}')

print(f'P(healthy & A): {A_healthy}')
print(f'P(healthy & C): {C_healthy}')
print(f'P(healthy & G): {G_healthy}')
print(f'P(healthy & T): {T_healthy}')

print("Sum of probabilities: ", sum([A_ill, C_ill, G_ill, T_ill, A_healthy, C_healthy, G_healthy, T_healthy]))


# #### Expected numbers


expected = {
    'ill & A': A_ill * ind_num,
    'ill & C': C_ill * ind_num,
    'ill & G': G_ill * ind_num,
    'ill & T': T_ill * ind_num,
    'healthy & A': A_healthy * ind_num,
    'healthy & C': C_healthy * ind_num,
    'healthy & G': G_healthy * ind_num,
    'healthy & T': T_healthy * ind_num
}

print(expected)


# #### Observed numbers


observed = {
    'ill & A': nuc_num["A"][1],
    'ill & C': nuc_num["C"][1],
    'ill & G': nuc_num["G"][1],
    'ill & T': nuc_num["T"][1],
    'healthy & A': nuc_num["A"][0],
    'healthy & C': nuc_num["C"][0],
    'healthy & G': nuc_num["G"][0],
    'healthy & T': nuc_num["T"][0]
}

print(observed)


# #### Functions definition


def error_func(expected, observed):
    return (expected - observed) ** 2 / expected

def error_func_dict(exp_dict, obs_dict):
    return sum([error_func(exp_dict[num], obs_dict[num]) for num in set(exp_dict) & set(obs_dict)])

observed_error = error_func_dict(expected, observed)
print(f'Error of given data sample: {observed_error}')

def simulate_one_sample(size):
    status = ["healthy", "ill"]
    status_prob = [healthy_prob, ill_prob]

    nucleotide = ["A", "C", "G", "T"]
    nucleotide_prob = [A_prob, C_prob, G_prob, T_prob]

    status_sample = np.random.choice(status, size=size, p=status_prob)
    nucleotide_sample  = np.random.choice(nucleotide,  size=size, p=nucleotide_prob)

    sample = [f'{status} & {nucleotide}' for status, nucleotide in zip(status_sample, nucleotide_sample)]

    return Counter(sample)


# #### Simulation


tries = 100000

errors = []
for try_ in range(tries):
    sim_sample = simulate_one_sample(ind_num)
    error = error_func_dict(expected, sim_sample)
    errors.append(error)


# #### Plot

bins = np.arange(min(errors), max(errors), 1)
ind_num, bins, patches = plt.hist(errors, bins=bins)

for i, bin in enumerate(bins[:-1]):
    if bin >= observed_error:
        patches[i].set_facecolor('tomato')
plt.show()


# #### p-value
bad_cases = np.sum([error > observed_error for error in errors])
print('p-value):', bad_cases / tries)


# ### Obtained p-value (0.99879) is higher than p-value threshold (0.05), so $H_0$ cannot be rejected.
