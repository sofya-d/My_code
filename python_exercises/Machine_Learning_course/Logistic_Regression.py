from sklearn.linear_model import LogisticRegression


with open("Module9_data1.txt", "r") as data:
    lines = list(data)

X = []
Y = []

for line in lines[1:]:
    row = line.strip().split(",")
    X.append([float(x) for x in row[1:12]])
    Y.append(int(row[13]))

print(f'X: {X[0:5]}', "\n", f'Y: {Y[0:5]}', sep = "\n")


with open("Module9_data2.txt", "r") as data:
    lines = list(data)

X_t = {}
X_t_list = []
Y_t = []

for line in lines[1:]:
    row = line.strip().split(",")
    X_t[row[0]] = [float(x) for x in row[1:12]]
    X_t_list.append([float(x) for x in row[1:12]])
    Y_t.append(int(row[12]))

print(f'X_t: {X_t}', "\n", f'Y_t: {Y_t}', sep = "\n")

log_reg = LogisticRegression(random_state = 2019, solver = 'lbfgs').fit(X, Y)


print(log_reg.classes_)


# ### 1


class_prob = log_reg.predict_proba([X_t["Warheads"]])
class_1_prob = class_prob[0][1]

print(f'The predicted probability for Warheads to class 1: {class_1_prob}')


# ### 2


class_prob = log_reg.predict_proba([X_t["Sugar Babies"]])
class_1_prob = class_prob[0][1]

print(f'The predicted probability for Sugar Babies to class 1: {class_1_prob}')


# ### Confusion matrix
# https://www.w3schools.com/python/python_ml_confusion_matrix.asp


predicted = list(log_reg.predict(X_t_list))

print(f'Actual: {Y_t}')
print(f'Predicted: {predicted}')


from sklearn import metrics


# ### 3


Precision = metrics.precision_score(Y_t, predicted)
print(f'Precision: {Precision}')


# ### 4

Recall = metrics.recall_score(Y_t, predicted)
print(f'Recall: {Recall}')


# ### 5


AUC = metrics.roc_auc_score(Y_t, log_reg.decision_function(X_t_list))
print(f'AUC: {AUC}')
