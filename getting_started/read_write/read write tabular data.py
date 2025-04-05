import pandas as pd

# pandas read_csv method
titanic = pd.read_csv("titanic.csv")
# titanic
print('titanic:\n', titanic)

# read first 8 rows
head_8 = titanic.head(8)
print('\nhead_8:\n', head_8)

# pandas dtypes attribute
# titanic.dtypes
print('\ntitanic.dtypes:\n', titanic.dtypes)

# pandas to_excel method
# titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

# pandas read_excel method
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

# titanic
print('titanic:\n', titanic)

# head
# read first 5 rows
head = titanic.head()
print('\nhead:\n', head)