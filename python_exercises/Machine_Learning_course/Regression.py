# ## Task 1


from sklearn.linear_model import LinearRegression
import statistics as st

X = []
Y = []

with open("Module7_Task1_data.txt", "r") as data:
    for line in data:
        row = line.split(",")
        X.append([int(row[1])])
        Y.append([int(row[2])])

print(f'X: {X}', f'Y: {Y}', sep = "\n")


print(f'Mean X: {st.mean([x[0] for x in X])}')
print(f'Mean Y: {st.mean([y[0] for y in Y])}')


reg = LinearRegression().fit(X, Y)


R2 = reg.score(X, Y)
print(f'R^2 of regression model: {R2}')


theta0 = reg.intercept_
print(f'Theta_0: {theta0[0]}')


theta1 = reg.coef_
print(f'Theta_1: {theta1[0][0]}')


# ## Task 2


with open("Module7_Task2_data.txt", "r") as data:
    lines = list(data)

X = []
Y = []

for line in lines[1:]:
    row = line.split(",")
    X.append([float(x) for x in row[1:12]])
    Y.append([float(row[12])])

print(f'X: {X[0:5]}', "\n", f'Y: {Y[0:5]}', sep = "\n")


reg = LinearRegression().fit(X, Y)


Dum_Dums_predictors = [[0, 1, 0, 0, 0, 0, 1, 0, 0, 0.73199999, 0.034000002]]
Nestle_Smarties_predictors = [[1, 0, 0, 0, 0, 0, 0, 0, 1, 0.26699999, 0.97600001]]
Candy_predictors = [[1, 1, 1, 1, 0, 1, 0, 0, 0, 0.128, 0.37]]


Dum_Dums_response = reg.predict(Dum_Dums_predictors)
Nestle_Smarties_response = reg.predict(Nestle_Smarties_predictors)
Candy_response = reg.predict(Candy_predictors)

print(f'Dum Dums predicted response: {Dum_Dums_response}')
print(f'Nestle Smarties predicted response: {Nestle_Smarties_response}')
print(f'Candy predicted response: {Candy_response}')
