# 8 combine_dataframes
# How to combine data from multiple tables
import pandas as pd

# 8.0 prerequisite

# 8.0.1 Air quality Nitrate data
air_quality_no2 = pd.read_csv("data/air_quality_no2_long.csv",
                              parse_dates=True)

air_quality_no2 = air_quality_no2[["date.utc", "location",
                                   "parameter", "value"]]

air_quality_no2_head = air_quality_no2.head()
print('air_quality_no2_head:\n', air_quality_no2_head)

# 8.0.2 Air quality Particulate matter data
air_quality_pm25 = pd.read_csv("data/air_quality_pm25_long.csv",
                               parse_dates=True)

air_quality_pm25 = air_quality_pm25[["date.utc", "location",
                                     "parameter", "value"]]

air_quality_pm25_head =air_quality_pm25.head()
print('air_quality_pm25_head:\n', air_quality_pm25_head)

# 8.1 Concatenating objects
print('\n## 8.1 Concatenating objects\n')

# 8.1.1 concat() function
# combine the measurements of NO2 and PM2.5 two tables with a similar structure, in a single table

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)

air_quality_head = air_quality.head()
print('air_quality_head:\n', air_quality_head)

print('Shape of the ``air_quality_pm25`` table: ', air_quality_pm25.shape)
print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)
print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)
