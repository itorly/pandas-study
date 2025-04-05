import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

# select a single column
ages = titanic["Age"]
print('ages:\n', ages)

type_age = type(ages)
print('type_age:\n', type_age)

shape_age = ages.shape
print('shape_age:\n', shape_age)

# select multiple columns
age_sex = titanic[["Age", "Sex"]]
print('age_sex:\n', age_sex)

type_age_sex = type(titanic[["Age", "Sex"]])
print('type_age_sex:\n', type_age_sex)

shape_age_sex = titanic[["Age", "Sex"]].shape
print('shape_age_sex:\n', shape_age_sex)