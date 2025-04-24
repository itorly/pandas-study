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

# By default, concatenation is along axis 0, so the resulting table combines the rows of the input tables.
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)

air_quality_axis_1 = pd.concat([air_quality_pm25, air_quality_no2], axis=1)
print('\nair_quality_axis_1:\n', air_quality_axis_1)

# 8.1.1.1 concat() function, axis = 0 and axis = 1
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

result_axis_0 = pd.concat([df1, df2], axis=0)
print('\nresult_axis_0:\n', result_axis_0)

result_axis_1 = pd.concat([df1, df2], axis=1)
print('\nresult_axis_1:\n', result_axis_1)


air_quality_head = air_quality.head()
print('air_quality_head:\n', air_quality_head)

print('Shape of the ``air_quality_pm25`` table: ', air_quality_pm25.shape)
print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)
print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)
