import pandas as pd
# 3 subset data
print('# 3 subset data\n')
titanic = pd.read_csv("data/titanic.csv")

# 3.1 select specific columns from a DataFrame
print('## 3.1 select specific columns from a DataFrame\n')

# 3.1.1 select a single column
print('## 3.1 select a single column\n')
ages = titanic["Age"]
print('ages:\n', ages)

type_age = type(ages)
print('type_age:\n', type_age)

shape_age = ages.shape
print('shape_age:\n', shape_age)

# 3.1.2 select multiple columns
print('## 3.2 select multiple columns\n')
age_sex = titanic[["Age", "Sex"]]
print('age_sex:\n', age_sex)

type_age_sex = type(titanic[["Age", "Sex"]])
print('type_age_sex:\n', type_age_sex)

shape_age_sex = titanic[["Age", "Sex"]].shape
print('shape_age_sex:\n', shape_age_sex)

# 3.2 filter specific rows from a DataFrame
# conditional expression or function
print('\n## 3.2 filter specific rows from a DataFrame\n')

# 3.2.1 conditional expression: greater than
print('### 3.2.1 conditional expression: greater than\n')
# The output of the conditional expression is
# a Series of boolean values
age_gt_35 = titanic["Age"] > 35
print('age_gt_35:\n', age_gt_35)

above_35 = titanic[age_gt_35]
print('\nabove_35:\n', above_35)

# above_35.shape
print('\nabove_35.shape:\n', above_35.shape)

# 3.2.2 conditional expression: equal, or
print('\n### 3.2.2 conditional expression: equal, or\n')
equal_to_2 = titanic["Pclass"] == 2
print('equal_to_2:\n', equal_to_2)

equal_to_2_or_3 = equal_to_2 | (titanic["Pclass"] == 3)
print('\nequal_to_2_or_3:\n', equal_to_2_or_3)

head_equal_to_2_or_3 = equal_to_2_or_3.head()
print('\nhead_equal_to_2_or_3:\n', head_equal_to_2_or_3)


# 3.2.3 conditional function: isin()
print('\n### 3.2.3 conditional function: isin()\n')

# check for which rows the Pclass column is either 2 or 3.
isin_2_3 = titanic["Pclass"].isin([2, 3])
print('isin_2_3:\n', isin_2_3)

titanic_2_3 = titanic[isin_2_3]
print('\ntitanic_2_3:\n', titanic_2_3)

head_2_3 = titanic_2_3.head()
print('\nhead_2_3:\n', head_2_3)


# 3.2.4 conditional function: notna()
print('\n### 3.2.4 conditional function: notna()\n')

notna = titanic["Age"].notna()
print('notna:\n', notna)

age_notna = titanic[notna]
print('\nage_notna:\n', age_notna)

head_age_notna = age_notna.head()
print('\nhead_age_notna:\n', head_age_notna)

shape_age_notna = age_notna.shape
print('\nshape_age_notna:\n', shape_age_notna)


# 3.3 select specific rows and columns from a DataFrame
print('\n## 3.3 select specific rows and columns from a DataFrame\n')

# 3.3.1 loc and iloc
print('### 3.3.1 loc and iloc\n')

# 3.3.1.1 select
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]
print('\nadult_names.head():\n', adult_names.head())

titanic_iloc_ = titanic.iloc[9:25, 2:5]
print('\ntitanic_iloc_:\n', titanic_iloc_)

# 3.3.1.2 assign
titanic.iloc[0:3, 3] = "anonymous"
names = titanic['Name']
print('\nnames:\n', names)

changed = titanic.iloc[0:3, 3]
print('\nchanged:\n', changed)
