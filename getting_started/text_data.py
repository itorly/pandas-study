# 10 text data
# How to manipulate textual data

import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

# 10.1 lowercase
print('# 10.1 lowercase\n')
# lower
lower = titanic["Name"].str.lower()
print('\nlower:\n', lower)
