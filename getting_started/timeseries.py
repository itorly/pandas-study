# 9 timeseries
# How to handle time series data with ease
import pandas as pd
import matplotlib.pyplot as plt

# 9.0 prerequisite: rename() function and unique() function
print("\n## 9.0 prerequisite: rename() function and unique() function")
air_quality = pd.read_csv("data/air_quality_no2_long.csv")
# rename() function
air_quality = air_quality.rename(columns={"date.utc": "datetime"})
air_quality_head = air_quality.head()
print('\nair_quality_head:\n', air_quality_head)

# unique() function
city_unique = air_quality.city.unique()
print('\ncity_unique:\n', city_unique)
