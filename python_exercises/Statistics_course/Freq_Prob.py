import scipy.stats
import matplotlib.pyplot as plt


# ### Frequency and probability of 1 in Ber(0.5) and Ber(0.1)


for p in [0.5, 0.1]:
    ber_dist = scipy.stats.bernoulli(p = p)

    tries_range = list(range(1, 1001))
    tries = []
    frequencies = []
    probabilities = []

    for tries_num in tries_range:
        try_ = ber_dist.rvs(size = 1)
        tries.append(try_)
        freq = sum(tries)
        prob = freq / tries_num
        frequencies.append(freq)
        probabilities.append(prob)
    
    fig = plt.figure(figsize=(15,5))

    ax1 = fig.add_subplot(121)
    ax1.plot(tries_range, frequencies)
    ax1.set_title(f'Frequency of 1 in Ber({p}) dependence on sample size')
    ax1.set_xlabel("Sample size")
    ax1.set_ylabel("Frequency of 1")

    ax2 = fig.add_subplot(122)
    ax2.plot(tries_range, probabilities)
    ax2.set_title(f'Probability of 1 in Ber({p}) dependence on sample size')
    ax2.set_xlabel("Sample size")
    ax2.set_ylabel("Probability of 1")
    
    plt.show()


# ### Frequency and probability of 4 and 7 in Pois(4)

from collections import Counter


for k in [4, 7]:
    pois_dist = scipy.stats.poisson(mu = 4)

    tries_range = list(range(1, 1001))
    tries = []
    frequencies = []
    probabilities = []

    for tries_num in tries_range:
        try_ = pois_dist.rvs(size = 1)
        tries.append(try_[0])
        freq = Counter(tries)[k]
        prob = freq / tries_num
        frequencies.append(freq)
        probabilities.append(prob)
    
    fig = plt.figure(figsize=(15,5))

    ax1 = fig.add_subplot(121)
    ax1.plot(tries_range, frequencies)
    ax1.set_title(f'Frequency of {k} in Pois(4) dependence on sample size')
    ax1.set_xlabel("Sample size")
    ax1.set_ylabel(f'Frequency of {k}')

    ax2 = fig.add_subplot(122)
    ax2.plot(tries_range, probabilities)
    ax2.set_title(f'Probability of {k} in Pois(4) dependence on sample size')
    ax2.set_xlabel("Sample size")
    ax2.set_ylabel(f'Probability of {k}')
    
    plt.show()


# ### It looks like probability of 1 in Ber(0.5) and probability of 4 in Pois(4) have higher convergence rate than probability of 1 in Ber(0.5) and probability of 7 in Pois(4) respectively.
