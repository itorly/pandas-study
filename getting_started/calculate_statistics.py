# 6 calculate_statistics
print('# 6 calculate_statistics\n')
# How to calculate summary statistics
import pandas as pd
titanic = pd.read_csv("data/titanic.csv")
head = titanic.head()
print('head:\n', head)

# 6.1 Aggregating statistics
print('\n## 6.1 Aggregating statistics\n')
# 6.1.1 average
age_mean = titanic["Age"].mean()
print('age_mean:\n', age_mean)

# 6.1.2 median
age_fare__median = titanic[["Age", "Fare"]].median()
print('age_fare__median:\n', age_fare__median)

# 6.1.3 describe function
describe = titanic[["Age", "Fare"]].describe()
print('\ndescribe:\n', describe)

# 6.1.4 agg function
agg = titanic.agg({"Age": ["min", "max", "median", "skew"], "Fare": ["min", "max", "median", "mean"], })
print('\nagg:\n', agg)

# 6.2 Aggregating statistics grouped by category
print('\n## 6.2 Aggregating statistics grouped by category\n')
mean = titanic[["Sex", "Age"]].groupby("Sex").mean()
print('mean:\n', mean)

sex__mean = titanic.groupby("Sex").mean(numeric_only=True)
print('sex__mean:\n', sex__mean)

age__mean = titanic.groupby("Sex")["Age"].mean()
print('age__mean:\n', age__mean)

fare__mean = titanic.groupby(["Sex", "Pclass"])["Fare"].mean()
print('fare__mean:\n', fare__mean)

