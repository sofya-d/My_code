salary = []
with open("exercise_data.csv") as file:
    lines = file.readlines()
    
for line in lines:
    row = line.rstrip().split(";")
    salary.append(int(row[1]))

print(salary[1:5])


import statistics as st


print(f'Salary mean is {st.mean(salary)}')


print(f'Salary variance is {st.variance(salary)}')


print(f'Salary population variance is {st.pvariance(salary)}')


print(f'Salary standard deviation is {st.stdev(salary)}')


print(f'Salary population standard deviation is {st.pstdev(salary)}')
