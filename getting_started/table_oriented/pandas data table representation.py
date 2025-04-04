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

