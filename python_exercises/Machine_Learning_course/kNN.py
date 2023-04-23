# ## Task 1
from sklearn.neighbors import KNeighborsClassifier


X = []
Cluster = []

with open("Module8_Task1_data.txt", "r") as data:
    lines = data.readlines()
    for line in lines:
        row = line.strip().split(",")
        x = int(row[1])
        y = int(row[2])
        cluster = int(row[3])
        
        X.append([x, y])
        Cluster.append(cluster)
        
print(f'X: {X}', end = "\n")
print(f'Clusters: {Cluster}', end = "\n")


# ### 1, 2


neigh = KNeighborsClassifier(n_neighbors = 5, p = 2)
neigh.fit(X, Cluster)


new_obj = [[52, 18]]


# #### 1

ans = neigh.kneighbors(new_obj, n_neighbors = 1, return_distance = True)
ans = ans[0][0][0]

print(f'The distance from the new object to the nearest neighbor using the Euclidean metric: {ans}')


# #### 2


ans = neigh.kneighbors(new_obj, n_neighbors = 3, return_distance = False)
ans = list(ans[0])
ans = [(i + 1) for i in ans]

print(f'The IDs of the three nearest points to new object for the Euclidean metric: {ans}')


# ### 3


neigh3 = KNeighborsClassifier(n_neighbors = 3, p = 2)
neigh3.fit(X, Cluster)


ans = neigh3.predict(new_obj)
ans = ans[0]

print(f'A class for the new object given 3 neighbors for the Euclidean metric: {ans}')


# ### 4


neighM = KNeighborsClassifier(n_neighbors = 5, p = 1)
neighM.fit(X, Cluster)

ans = neighM.kneighbors(new_obj, n_neighbors = 1, return_distance = True)
ans = ans[0][0][0]

print(f'The distance from the new object to the nearest neighbor using the Manhattan distance: {ans}')


# ### 5


ans = neighM.kneighbors(new_obj, n_neighbors = 3, return_distance = False)
ans = list(ans[0])
ans = [(i + 1) for i in ans]

print(f'The IDs of the three nearest points to new object for the Manhattan distance: {ans}')


# ### 6


neighM3 = KNeighborsClassifier(n_neighbors = 3, p = 1)
neighM3.fit(X, Cluster)

ans = neighM3.predict(new_obj)
ans = ans[0]

print(f'A class for the new object given 3 neighbors for the Manhattan distance: {ans}')


# ## Task 2

# ### 1


spam_num = 30
ham_num = 29

mail_num = spam_num + ham_num

spam_prob = spam_num / mail_num
ham_prob = ham_num / mail_num

print(f'The probability that the email is SPAM based on the training set: {spam_prob}')


# ### 2, 3


word_oc_spam = [4, 2, 0, 0, 1, 3, 4, 16, 32, 37]
word_oc_ham = [1, 3, 4, 9, 11, 21, 42, 9, 0, 0]

spam_word_num = sum(word_oc_spam)
ham_word_num = sum(word_oc_ham)

uniq_word_num = len(word_oc_spam)


word_mail_spam = [4, 0, 16, 0, 3, 0, 37]
word_mail_ham = [42, 0, 9, 0, 21, 9, 0]

out_dict = 2


P_X_Spams = []
for word_num in word_mail_spam:
    P_X_Spam = (word_num + 1) / (spam_word_num + uniq_word_num + out_dict)
    P_X_Spams.append(P_X_Spam)

P_X_Hams = []
for word_num in word_mail_ham:
    P_X_Ham = (word_num + 1) / (ham_word_num + uniq_word_num + out_dict)
    P_X_Hams.append(P_X_Ham)


import math


F_spam = math.log(spam_prob)
for prob in P_X_Spams:
    F_spam += math.log(prob)

F_ham = math.log(ham_prob)
for prob in P_X_Hams:
    F_ham += math.log(prob)

print(f'F(spam) = {F_spam}')
print(f'F(ham) = {F_ham}')


# ### 4


e = math.e
P_mail_spam = 1 / (1 + e**(F_ham - F_spam))
print(f'The probability that the email is SPAM: {P_mail_spam}')
