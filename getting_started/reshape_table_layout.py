# 7 reshape_table_layout
import pandas as pd

titanic = pd.read_csv("data/titanic.csv")
titanic_head = titanic.head()
print('titanic_head:\n', titanic_head)

air_quality = pd.read_csv(
    "data/air_quality_long.csv", index_col="date.utc", parse_dates=True
)
air_quality_head = air_quality.head()
print('air_quality_head:\n', air_quality_head)

# 7.1 Sort table rows
titanic_sort_values_by_age = titanic.sort_values(by="Age")
head_of_titanic_sort_values_by_age = titanic_sort_values_by_age.head()
print('\nhead_of_titanic_sort_values_by_age:\n', head_of_titanic_sort_values_by_age)

titanic_sort_values_by_Pclass_and_age = titanic.sort_values(by=['Pclass', 'Age'], ascending=False)
head_of_titanic_sort_values_by_Pclass_and_age = titanic_sort_values_by_Pclass_and_age.head()
print('\nhead_of_titanic_sort_values_by_Pclass_and_age:\n', head_of_titanic_sort_values_by_Pclass_and_age)

