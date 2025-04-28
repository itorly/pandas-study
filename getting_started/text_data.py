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

# 10.3 contains and indexing
print('# 10.3 contains and indexing\n')
# contains
contains = titanic["Name"].str.contains("Countess")
print('\ncontains:\n', contains)
# indexing
contains_records = titanic[titanic["Name"].str.contains("Countess")]
print('\ncontains_records:\n', contains_records)

# 10.4 len, idmax and loc
print('# 10.4 len, idmax and loc\n')
# len
len = titanic["Name"].head().str.len()
print('\nlen:\n', len)

# idxmax, the id of the maximum length
idxmax = titanic["Name"].head().str.len().idxmax()
print('\nidxmax:\n', idxmax)

# loc
loc = titanic.loc[titanic["Name"].str.len().idxmax(), "Name"]
print('\nloc:\n', loc)

# 10.5 replace
print('# 10.5 replace\n')
titanic["Sex_short"] = titanic["Sex"].replace({"male": "M", "female": "F"})
print('\ntitanic["Sex_short"]:\n', titanic["Sex_short"])