# ## Types of variables in given data
# ### column name: variable type: variable subtype
# #### "sex": categorical: nominal
# #### "age": numeric: continuous
# #### "Time": numeric: continuous
# #### "Number_of_Warts": numeric: discrete
# #### "Type": categorical: nominal
# #### "Area": numeric: continuous
# #### "induration_diameter": numeric: continuous
# #### "Result_of_Treatment": categorical: nominal

# The variables "Age", "Time", "Area" and "Induration_diameter" can also be considered discrete if someone specifies how precise to measure them. For example, if there is no specification, "Age" could be measured with milisecond precision and more. But if someone specifies that "Age" could be only the number of whole years a person has lived, then it should be considered a discrete variable.

# ### Set-up

import pandas as pd
import matplotlib.pyplot as plt
import seaborn


plt.rcParams['figure.figsize'] = [9, 4]
plt.rcParams['figure.dpi'] = 100


# ### Import data

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00428/Immunotherapy.xlsx"
data = pd.read_excel(io=url)


# ### Pair plot
seaborn.pairplot(data)


# #### It is does not look like here is any correlation between different variables.

# ### Response to treatment (nominal variable) vs Sex (nominal variable) comparison (stacked barplot)
row_num = data.shape[0]
Sex_Treatment_Response = {1: [0, 0], 2: [0, 0]}

for i in range(row_num):
    sex = data._get_value(index=i, col="sex")
    response = data._get_value(index=i, col="Result_of_Treatment")
    if response == 0:
        Sex_Treatment_Response[sex][0] += 1
    else:
        Sex_Treatment_Response[sex][1] += 1

print(Sex_Treatment_Response) # first value in list is "No", second is "Yes"


Sex_Treat_Resp = []
for key in Sex_Treatment_Response.keys():
    lst = [key]
    lst += Sex_Treatment_Response[key]
    Sex_Treat_Resp.append(lst)

print(Sex_Treat_Resp)


Sex = [f'gender{lst[0]}' for lst in Sex_Treat_Resp]
No = [lst[1] for lst in Sex_Treat_Resp]
Yes = [lst[2] for lst in Sex_Treat_Resp]

width = 0.35

fig, ax = plt.subplots()

ax.bar(Sex, No, width, label='No')
ax.bar(Sex, Yes, width, bottom=No, label='Yes')

ax.set_xlabel('Sex')
ax.set_ylabel('Number of patients')
ax.set_title('Sex differences in treatment response')
ax.legend(title="Treatment response")

plt.show()


# #### Here is a slight difference in percentage of positive treatment response between males and females. But it is too early to make any conclusions because we have to at least normalise sample sizes before comparing percentage of treatment responses.

# ### Response to treatment (nominal variable) vs Age (numeric variable) comparison (stacked barplot)


row_num = data.shape[0]
Age_Treatment_Response = {}

for i in range(row_num):
    age = data._get_value(index=i, col="age")
    response = data._get_value(index=i, col="Result_of_Treatment")
    if age not in Age_Treatment_Response.keys():
        Age_Treatment_Response[age] = [0, 0]
        if response == 0:
            Age_Treatment_Response[age][0] += 1
        else:
            Age_Treatment_Response[age][1] += 1
    else:
        if response == 0:
            Age_Treatment_Response[age][0] += 1
        else:
            Age_Treatment_Response[age][1] += 1

print(Age_Treatment_Response) # first value in list is "No", second is "Yes"


Age_Treat_Resp = []
for key in Age_Treatment_Response.keys():
    lst = [key]
    lst += Age_Treatment_Response[key]
    Age_Treat_Resp.append(lst)

def first_element(lst):
    return lst[0]

Age_Treat_Resp.sort(key=first_element)

print(Age_Treat_Resp)


Age = [str(lst[0]) for lst in Age_Treat_Resp]
No = [lst[1] for lst in Age_Treat_Resp]
Yes = [lst[2] for lst in Age_Treat_Resp]

width = 0.35


fig, ax = plt.subplots(figsize = (12, 4))

ax.bar(Age, No, width, label='No')
ax.bar(Age, Yes, width, bottom=No, label='Yes')

ax.set_xlabel('Age')
ax.set_ylabel('Number of patients')
ax.set_title('Age differences in treatment response')
ax.legend(title="Treatment response")

plt.show()


# #### We could speculate that patients of age from 16 to 25 years old have a better response to treatment. But it is too early to make any coclusions because each age sample size is too small so the observed values may result because of random events. Also I do not see any clear dependence of treatment response on age.

# ### Number of warts (numeric variable) vs Age (numeric variable) comparison (scatter plot)
warts_num = list(data["Number_of_Warts"])
age = list(data["age"])


plt.scatter(age, warts_num)
plt.xlabel('Age')
plt.ylabel('Number of warts')
plt.title('Warts number dependence on age')

plt.show()


# #### This scatter plot shows that number of warts does not depend on age.
