import pandas as pd
# 3 subset data
print('# 3 subset data\n')
titanic = pd.read_csv("data/titanic.csv")

# 3.1 select a single column
print('## 3.1 select a single column\n')
ages = titanic["Age"]
print('ages:\n', ages)

type_age = type(ages)
print('type_age:\n', type_age)

shape_age = ages.shape
print('shape_age:\n', shape_age)

# 3.2 select multiple columns
print('## 3.2 select multiple columns\n')
age_sex = titanic[["Age", "Sex"]]
print('age_sex:\n', age_sex)

type_age_sex = type(titanic[["Age", "Sex"]])
print('type_age_sex:\n', type_age_sex)

shape_age_sex = titanic[["Age", "Sex"]].shape
print('shape_age_sex:\n', shape_age_sex)

# 3.3 conditional expression or function
print('\n## 3.3 conditional expression or function\n')

