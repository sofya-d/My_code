import pandas as pd
import scipy
from scipy import stats


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00428/Immunotherapy.xlsx"
data = pd.read_excel(io=url)


treat_res_1 = data[data["Result_of_Treatment"] == 1]


treat_res_0 = data[data["Result_of_Treatment"] == 0]
area_1 = treat_res_1["Area"]
area_0 = treat_res_0["Area"]


scipy.stats.kstest(area_1, area_0)


# #### p-value (~ 0.88) is greater than threshold (0.05) so $H_0$ can't be rejected. Hense groups with different result of treatment have the same distribution of wart area.

# ## Task 2


import numpy as np
import scipy
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt


np.random.seed(42)


def calc_step(min_mean, max_mean, dec):
    if min_mean < 0 and max_mean > 0:
        mean_range = abs(min_mean) + max_mean
    elif min_mean < 0 and max_mean < 0:
        mean_range = abs(min_mean + max_mean)
    else:
        mean_range = max_mean - min_mean
    step = round((mean_range / 20), dec)
    return step


# ### Uniform


def calc_mean_uniform(sample_size):
    dist = scipy.stats.uniform.rvs(size=sample_size)
    return np.mean(dist)
    

sample_size = 1000
sample_num = 10_000

means = np.array([calc_mean(sample_size) for _ in range(sample_num)])

min_mean = min(means)
max_mean = max(means)
dec = 3
step = calc_step(min_mean, max_mean, dec)
sns.histplot(means, bins=np.arange(min_mean, max_mean, step));


theor_dist = scipy.stats.uniform()
theor_mean = theor_dist.stats(moments="m")
theor_stdev = np.sqrt(theor_dist.stats(moments="v"))
print(theor_mean)
print(theor_stdev)


scipy.stats.kstest(means, 'norm', args=(theor_mean, theor_stdev / np.sqrt(sample_size)))


# ### Normal


def calc_mean_norm(sample_size):
    dist = scipy.stats.norm.rvs(size=sample_size)
    return np.mean(dist)


sample_size = 1000
sample_num = 10_000

means = np.array([calc_mean(sample_size) for _ in range(sample_num)])

min_mean = min(means)
max_mean = max(means)
dec = 2
step = calc_step(min_mean, max_mean, dec)
sns.histplot(means, bins=np.arange(min_mean, max_mean, step));


theor_dist = scipy.stats.norm()
theor_mean = theor_dist.stats(moments="m")
theor_stdev = np.sqrt(theor_dist.stats(moments="v"))
print(theor_mean)
print(theor_stdev)


scipy.stats.kstest(means, 'norm', args=(theor_mean, theor_stdev / np.sqrt(sample_size)))


# ### Exponantial


def calc_mean_expon(sample_size):
    dist = scipy.stats.expon.rvs(size=sample_size)
    return np.mean(dist)


sample_size = 1000
sample_num = 10_000

means = np.array([calc_mean(sample_size) for _ in range(sample_num)])

min_mean = min(means)
max_mean = max(means)
dec = 2
step = calc_step(min_mean, max_mean, dec)
sns.histplot(means, bins=np.arange(min_mean, max_mean, step));

theor_dist = scipy.stats.expon()
theor_mean = theor_dist.stats(moments="m")
theor_stdev = np.sqrt(theor_dist.stats(moments="v"))
print(theor_mean)
print(theor_stdev)


scipy.stats.kstest(means, 'norm', args=(theor_mean, theor_stdev / np.sqrt(sample_size)))


# ### Cauchy

# #### Central limit theorem doesn’t apply to distributions with infinite variance, such as the Cauchy distribution.

# ### Convergence rate

sample_sizes = list(range(10, 1001, 10))
sample_num = 10_000
ks_pvals_uniform = []
ks_pvals_norm = []
ks_pvals_expon = []
for sample_size in sample_sizes:
    means = np.array([calc_mean_uniform(sample_size) for _ in range(sample_num)])
    theor_dist = scipy.stats.uniform()
    theor_mean = theor_dist.stats(moments="m")
    theor_stdev = np.sqrt(theor_dist.stats(moments="v"))
    ks_res = scipy.stats.kstest(means, 'norm', args=(theor_mean, theor_stdev / np.sqrt(sample_size)))
    ks_pval = list(ks_res)[1]
    ks_pvals_uniform.append(ks_pval)
    
    means = np.array([calc_mean_norm(sample_size) for _ in range(sample_num)])
    theor_dist = scipy.stats.norm()
    theor_mean = theor_dist.stats(moments="m")
    theor_stdev = np.sqrt(theor_dist.stats(moments="v"))
    ks_res = scipy.stats.kstest(means, 'norm', args=(theor_mean, theor_stdev / np.sqrt(sample_size)))
    ks_pval = list(ks_res)[1]
    ks_pvals_norm.append(ks_pval)
    
    means = np.array([calc_mean_expon(sample_size) for _ in range(sample_num)])
    theor_dist = scipy.stats.expon()
    theor_mean = theor_dist.stats(moments="m")
    theor_stdev = np.sqrt(theor_dist.stats(moments="v"))
    ks_res = scipy.stats.kstest(means, 'norm', args=(theor_mean, theor_stdev / np.sqrt(sample_size)))
    ks_pval = list(ks_res)[1]
    ks_pvals_expon.append(ks_pval)


fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(17,4))

ax[0].set(title='Uniform', ylabel = "p-value")
ax[0].plot(sample_sizes, ks_pvals_uniform)

ax[1].set(title='Normal', xlabel = "sample size")
ax[1].plot(sample_sizes, ks_pvals_norm)

ax[2].set(title='Exponential')
ax[2].plot(sample_sizes, ks_pvals_expon)
    
plt.show()


# #### Plots show that distribution of normal distribution means has the highest speed of convergence and distribution of exponential distribution means has the lowest speed of convergence.
