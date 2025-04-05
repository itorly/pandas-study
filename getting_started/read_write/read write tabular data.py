import pandas as pd

# pandas read_csv method
titanic = pd.read_csv("titanic.csv")
# titanic
print('titanic:\n', titanic)

# pandas dtypes attribute
# titanic.dtypes
print('\ntitanic.dtypes:\n', titanic.dtypes)

# pandas to_excel method
titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

# pandas read_excel method
titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

# titanic
print('titanic:\n', titanic)