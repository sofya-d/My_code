import pandas as pd
import scipy
import seaborn as sns
import matplotlib.pyplot as plt


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00428/Immunotherapy.xlsx"
data = pd.read_excel(io=url)
data


# # 1

# ### $H_0$ - number of warts does not correlate with age
# ### $H_1$ - number of warts correlates with age
# 
# #### I expect to see positive correlation between age and number of warts. Older people have less effective immune system. An older man also can be ill for a longer time than younger man hense they can have more warts.

age = data["age"]
warts_num = data["Number_of_Warts"]

sns.regplot(x = age, y = warts_num).set(title = "Warts number dependency on age")


# #### The scatter plot shows no correlation between age and biggest wart area. But I still want to make sure that there is no correlation.
# #### I choose Kendall's correlation coefficient tau for assessment because it's assumptions are only continuous/ordinal variable type and monotonicity. Also it can catch non-linear correlation.

result = scipy.stats.kendalltau(age, warts_num)
print("r correlation coefficient:", float(result[0]))
print("p-value:", result[1])


# ### The result of Kendall's correlation test shows no correlation between age and warts number, hense I can not reject $H_0$.

# # 2

# ### $H_0$ - area of the biggest wart does not correlate with age
# ### $H_1$ - area of the biggest wart correlates with age
# 
# #### I expect to see positive correlation between age and number of warts. Older people have less effective immune system. An older man also can be ill for a longer time than younger man hense they can have more warts.

age = data["age"]
area = data["Area"]

sns.regplot(x = age, y = area).set(title = "Biggest wart area dependency on age")


# #### The scatter plot shows insignificant negative correlation between age and biggest wart area. But I still want to make sure that there is no correlation.
# #### I choose Kendall's correlation coefficient tau for assessment because it's assumptions are only continuous/ordinal variable type and monotonicity. Also it can catch non-linear correlation.

result = scipy.stats.kendalltau(age, area)
print("r correlation coefficient:", float(result[0]))
print("p-value:", result[1])


# ### The result of Kendall's correlation test shows no correlation between age and biggest wart area, hense I can not reject $H_0$.

# # 3 Kolmogorov-Smirnov test

# ### $H_0$ - time elapsed before treatment does not affect treatment result distribution
# ### $H_1$ - time elapsed before treatment affects treatment result distribution
# ### p-value threshold = 0.05


time_0 = data[data["Result_of_Treatment"] == 0]
time_0 = time_0["Time"]

time_1 = data[data["Result_of_Treatment"] == 1]
time_1 = time_1["Time"]


sns.histplot(data=time_0, color="skyblue", label="0", kde=True)
sns.histplot(data=time_1, color="red", label="1", kde=True)

plt.legend() 
plt.show()


# #### Samples distributions are not normal and do not have similar shape. They look like they are completely different. I will apply Kolmogorov-Smirnov test to check it.

scipy.stats.kstest(time_0, time_1)


# #### I also can use nonparametric equivalent of t test that is suitable for different distributions -- Mann-Whitney U test with mean ranks (instead of medians). But I failed to find this test implementation in Python.

# ### According to KS test here is significant difference between distribution of time sample with negative treatment result and distribution of time sample with positive treatment result. I reject $H_0$, hense time elapsed from treatment begining affects treatment result.

# # 4 Kolmogorov-Smirnov test

# ### $H_0$ - age affects treatment result distribution
# ### $H_1$ - age does not affect treatment result distribution
# ### p-value threshold = 0.05


age_0 = data[data["Result_of_Treatment"] == 0]
age_0 = age_0["age"]

age_1 = data[data["Result_of_Treatment"] == 1]
age_1 = age_1["age"]


sns.histplot(data=age_0, color="skyblue", label="0", kde=True)
sns.histplot(data=age_1, color="red", label="1", kde=True)

plt.legend() 
plt.show()


# #### Samples distributions are not normal and do not have similar shape. They look like they are completely different. I will apply Kolmogorov-Smirnov test to check it.

scipy.stats.kstest(age_0, age_1)


# #### I also can use nonparametric equivalent of t test that is suitable for different distributions -- Mann-Whitney U test with mean ranks (instead of medians). But I failed to find this test implementation in Python.

# ### According to KS test here is significant difference between distribution of time sample with negative treatment result and distribution of time sample with positive treatment result. I reject $H_0$, hense time elapsed from treatment begining affects treatment result.

# # 5 chi square test

# ### $H_0$ - gender does not affect treatment result
# ### $H_1$ - gender affects treatment result


sex1 = data[data["sex"] == 1]
sex1_treatment0 = sex1[sex1["Result_of_Treatment"] == 0].shape[0]
sex1_treatment1 = sex1[sex1["Result_of_Treatment"] == 1].shape[0]

sex2 = data[data["sex"] == 2]
sex2_treatment0 = sex2[sex2["Result_of_Treatment"] == 0].shape[0]
sex2_treatment1 = sex2[sex2["Result_of_Treatment"] == 1].shape[0]


d = {'col1': [1, 2], 'col2': [3, 4]}
contingency = pd.DataFrame(data={"sex": [1, 2], "treatment_0": [sex1_treatment0, sex2_treatment0], "treatment_1": [sex1_treatment1, sex2_treatment1]})
contingency


expected = scipy.stats.chi2_contingency(contingency.iloc[:,1:].values)
expected


# ### Test shows there is no significant difference in treatnment results, hense $H_0$ can not be rejected.
