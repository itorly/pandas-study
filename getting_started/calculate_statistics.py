# 6 calculate_statistics
print('# 6 calculate_statistics\n')
# How to calculate summary statistics
import pandas as pd
titanic = pd.read_csv("data/titanic.csv")
head = titanic.head()
print('head:\n', head)

# 6.1 average
age_mean = titanic["Age"].mean()
print('age_mean:\n', age_mean)

# 6.2 median
age_fare__median = titanic[["Age", "Fare"]].median()
print('age_fare__median:\n', age_fare__median)

# 6.3 describe function
describe = titanic[["Age", "Fare"]].describe()
print('\ndescribe:\n', describe)

# 6.4 agg function
agg = titanic.agg({"Age": ["min", "max", "median", "skew"], "Fare": ["min", "max", "median", "mean"], })
print('\nagg:\n', agg)
