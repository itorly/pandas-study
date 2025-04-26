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

# 9.1 Using pandas datetime properties
print("\n## 9.1 Using pandas datetime properties")

# 9.1.1 convert to datetime
print("\n## 9.1.1 convert to datetime")
# 9.1.1.1 to_datetime() function
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
air_quality_datetime = air_quality["datetime"]
print('\nair_quality_datetime:\n', air_quality_datetime)

# 9.1.1.2 parse_dates parameter of read_csv() or read_json() function
read_csv_and_convert_to_datetime = pd.read_csv("data/air_quality_no2_long.csv", parse_dates=["date.utc"])
print('\nread_csv_and_convert_to_datetime:\n', read_csv_and_convert_to_datetime)

