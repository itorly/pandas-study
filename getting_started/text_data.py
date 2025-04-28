# 10 text data
# How to manipulate textual data

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

# 10.1 lowercase
print('# 10.1 lowercase\n')
# lower
lower = titanic["Name"].str.lower()
print('\nlower:\n', lower)

# 10.2 split and get
print('# 10.2 split and get\n')
# split
split = titanic["Name"].str.split(",")
print('\nsplit:\n', split)

# get
titanic["Surname"] = titanic["Name"].str.split(",").str.get(0)
print('\ntitanic["Surname"]:\n', titanic["Surname"])
