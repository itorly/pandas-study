# 7 reshape_table_layout
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("data/titanic.csv")
titanic_head = titanic.head()
print('titanic_head:\n', titanic_head)

air_quality = pd.read_csv(
    "data/air_quality_long.csv", index_col="date.utc", parse_dates=True
)
air_quality_head = air_quality.head()
print('air_quality_head:\n', air_quality_head)

# 7.1 Sort table rows
print('\n## 7.1 Sort table rows\n')
head_of_titanic_sort_values_by_age = titanic.sort_values(by="Age").head()
print('\nhead_of_titanic_sort_values_by_age:\n', head_of_titanic_sort_values_by_age)

head_of_titanic_sort_values_by_Pclass_and_age = titanic.sort_values(by=['Pclass', 'Age'], ascending=False).head()
print('\nhead_of_titanic_sort_values_by_Pclass_and_age:\n', head_of_titanic_sort_values_by_Pclass_and_age)


# 7.2 Long to wide table format
print('\n## 7.2 Long to wide table format\n')

# 7.2.1 subset: ==, sort_index(), groupby()
# filter for no2 data only
no2 = air_quality[air_quality["parameter"] == "no2"]

# use 2 measurements (head) for each location (groupby)
no2_subset = no2.sort_index().groupby(["location"]).head(2)

print('\nno2_subset:\n', no2_subset)

# 7.2.2 pivot() function
# The pivot() function is purely reshaping of the data: a single value for each index/column combination is required.
pivot = no2_subset.pivot(columns="location", values="value")
print('\npivot:\n', pivot)

plot = no2.pivot(columns="location", values="value").plot()
print('\nplot:\n', plot)
plt.show()