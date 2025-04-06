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

# 3.3.1 conditional expression: greater than
print('### 3.3.1 conditional expression: greater than\n')
# The output of the conditional expression is
# a Series of boolean values
age_gt_35 = titanic["Age"] > 35
print('age_gt_35:\n', age_gt_35)

above_35 = titanic[age_gt_35]
print('\nabove_35:\n', above_35)

# above_35.shape
print('\nabove_35.shape:\n', above_35.shape)

# 3.3.2 conditional expression: equal, or
print('\n### 3.3.2 conditional expression: equal, or\n')
equal_to_2 = titanic["Pclass"] == 2
print('equal_to_2:\n', equal_to_2)

equal_to_2_or_3 = equal_to_2 | (titanic["Pclass"] == 3)
print('\nequal_to_2_or_3:\n', equal_to_2_or_3)

head_equal_to_2_or_3 = equal_to_2_or_3.head()
print('\nhead_equal_to_2_or_3:\n', head_equal_to_2_or_3)

