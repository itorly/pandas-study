import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

# select a single column
ages = titanic["Age"]
print('ages:\n', ages)

type_age = type(ages)
print('type_age:\n', type_age)

shape_age = ages.shape
print('shape_age:\n', shape_age)
