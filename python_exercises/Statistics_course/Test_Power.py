# Calculate statistical power:
# https://stattrek.com/hypothesis-test/statistical-power
# 
# Introduction to power analysis: https://www.geeksforgeeks.org/introduction-to-power-analysis-in-python/
# 
# Independent t-test = 2-sample t-test.

from statsmodels.stats.power import TTestPower
import matplotlib.pyplot as plt
import numpy as np


# ## Test power dependency on:

# ### a) Sample size


sd = 10
# p-value
alpha = 0.05
# mu = mean
H0_mu = 110
H1_mu = 120
effect_size = (H1_mu - H0_mu) / sd
test_power_obj = TTestPower()

print("Effect size:", effect_size)


# n = sample size
ns = list(range(1, 101))
test_powers = []
for n in ns:
    test_power = test_power_obj.power(nobs = n, effect_size = effect_size, alpha = alpha)
    test_powers.append(test_power)


plt.plot(ns, test_powers)
plt.xlabel('Sample size')
plt.ylabel('Power of test')
plt.show()


# ### b) $H_1$


# sample size
n = 42
sd = 10
# p-value
alpha = 0.05
# mu = mean
H0_mu = 110
test_power_obj = TTestPower()


H1_mus = list(np.arange(100, 121, 0.1))
test_powers = []
for H1_mu in H1_mus:
    effect_size = (H1_mu - H0_mu) / sd
    test_power = test_power_obj.power(nobs = n, effect_size = effect_size, alpha = alpha)
    test_powers.append(test_power)


plt.plot(H1_mus, test_powers)
plt.xlabel('Alternative hypothesis mean')
plt.ylabel('Power of test')
plt.show()


# ### c) p-value threshold (alpha)


# sample size
n = 30
sd = 10
# mu = mean
H0_mu = 110
H1_mu = 120
effect_size = (H1_mu - H0_mu) / sd
test_power_obj = TTestPower()


alphas = list(np.arange(0.001, 0.1, 0.001))
test_powers = []
for alpha in alphas:
    test_power = test_power_obj.power(nobs = n, effect_size = effect_size, alpha = alpha)
    test_powers.append(test_power)

plt.plot(alphas, test_powers)
plt.xlabel('p-value threshold')
plt.ylabel('Power of test')
plt.show()


# ### d) Standard deviation


# sample size
n = 21
# p-value
alpha = 0.05
# mu = mean
H0_mu = 110
H1_mu = 120
test_power_obj = TTestPower()


sds = list(np.arange(5, 50, 0.5))
test_powers = []
for sd in sds:
    effect_size = (H1_mu - H0_mu) / sd
    test_power = test_power_obj.power(nobs = n, effect_size = effect_size, alpha = alpha)
    test_powers.append(test_power)


plt.plot(sds, test_powers)
plt.xlabel('Standard deviation')
plt.ylabel('Power of test')
plt.show()
