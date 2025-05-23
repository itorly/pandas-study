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
# plt.show()

# 7.3 Pivot table
print('\n## 7.3 Pivot table\n')
pivot_table = air_quality.pivot_table(values="value", index="location", columns="parameter", aggfunc="mean")
print('\npivot_table:\n', pivot_table)

pivot_table_with_margins =air_quality.pivot_table(
    values="value",
    index="location",
    columns="parameter",
    aggfunc="mean",
    margins=True,
)
print('\npivot_table_with_margins:\n', pivot_table_with_margins)

same_result = air_quality.groupby(["parameter", "location"])[["value"]].mean()
print('\nsame_result:\n', same_result)


# 7.4 Wide to long format
print('\n## 7.4 Wide to long format\n')

# 7.4.1 reset_index() function
no2_pivoted = no2.pivot(columns="location", values="value").reset_index()
pivoted_head = no2_pivoted.head()
print('\npivoted_head:\n', pivoted_head)

# 7.4.2 melt() function
no_2 = no2_pivoted.melt(id_vars="date.utc")
no_2_head = no_2.head()
print('\nno_2_head:\n', no_2_head)

no_2 = no2_pivoted.melt(
    id_vars="date.utc",
    # value_vars defines which columns to melt together
    value_vars=["BETR801", "FR04014", "London Westminster"],
    # value_name provides a custom column name for the values column
    # instead of the default column name value
    value_name="NO_2",
    # var_name provides a custom column name for the column collecting
    # the column header names.
    # Otherwise, it takes the index name or a default variable
    var_name="id_location",
)
no_2_head = no_2.head()
print('\nno_2_head:\n', no_2_head)