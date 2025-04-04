import pandas as pd

df = pd.DataFrame(
    {
        "Name": [
            "Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [22, 35, 58],
        "Sex": ["male", "male", "female"],
    }
)

# df
print('df:\n', df)

# When selecting a single column of a pandas DataFrame,
# the result is a pandas Series.
# df["Age"]
print('df["Age"]:\n', df["Age"])

# create a Series from scratch
ages = pd.Series([22, 35, 58], name="Age")


# typical functions a DataFrame
# df.info()
print('\ndf.info():\n', df.info())

# df.describe()
print('\ndf.describe():\n', df.describe())

# ages.max()
print('\nages.max():\n', ages.max())

# df.head()
print('\ndf.head():\n', df.head())

# df.tail()
print('\ndf.tail():\n', df.tail())


# typical functions a Series
# ages.info()
print('\nages.info():\n', ages.info())

# ages.describe()
print('\nages.describe():\n', ages.describe())

# df["Age"].max()
print('\ndf["Age"].max():\n', df["Age"].max())

# ages.head()
print('\nages.head():\n', ages.head())

# ages.tail()
print('\nages.tail():\n', ages.tail())
