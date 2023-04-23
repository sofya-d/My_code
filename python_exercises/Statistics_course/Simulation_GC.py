# # HW4, Task1

# ## Given:
# 
# #### Organism distribution of nucleotides (GC content = 70%):
# 
# | A   | C   | G   | T   |
# |-----|-----|-----|-----|
# | 15% | 35% | 35% | 15% |
# 
# #### Nucleotide number in given sequence with length 400.
# 
# | A   | C   | G   | T   |
# |-----|-----|-----|-----|
# | 48  | 164 | 129 | 59  |
# 
# #### p-value threshold = 0.05

# ## Hipotheses
# 
# $H_0$ — given sequence GC content is 70%  
# $H_1$ — given sequence GC content is not 70%

# ## Solution

# #### Set-up


import numpy as np
import matplotlib.pyplot as plt

from collections import Counter

plt.rcParams['figure.figsize'] = [7, 3]
plt.rcParams['figure.dpi'] = 100


# #### Definition of function that yields random sequence with ~70% GC-content of input length.


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


# #### Definition of function that calculates error.


def error_func(exprected, observed):
    return (exprected - observed) ** 2 / exprected


# #### The code below: 1) generates random sequence with length 400 and GC-content ~70%; 2) Calculates frquences of nucleotides in random sequences; 3) calculates error; 4) appends error to the list "errors".

sim_num = 100000
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


# #### The code below calculates error of given sequence and writes it into variable "given_seq_error".


given_seq_nuc_num = {
    'A': 48,
    'C': 164,
    'G': 129,
    'T': 59,
}

given_seq_error = 0
for nucleotide in nucleotides:
    if nucleotide in "GC":
            expected = seq_len * 0.35
    else:
        expected = seq_len * 0.15
    
    observed = given_seq_nuc_num[nucleotide]
    given_seq_error += error_func(expected, observed)


# #### Plot drawing.


bins = np.arange(min(errors), max(errors), 1)
seq_len, bins, patches = plt.hist(errors, bins=bins)

for i, bin in enumerate(bins[:-1]):
    if bin >= given_seq_error:
        patches[i].set_facecolor('tomato')
plt.show()


# #### p-value calculation.


higher_errors = np.sum([error > given_seq_error for error in errors])
print('p-value:', higher_errors / sim_num)


# ## Answer
# 
# ### Obtained p-value, 0.06062, is greater than the given p-value threshold, 0.05.
# ### Hense, $H_0$ cannot be rejected.
