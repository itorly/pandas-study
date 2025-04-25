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

air_quality_pm25_head = air_quality_pm25.head()
print('air_quality_pm25_head:\n', air_quality_pm25_head)

# 8.1 Concatenating objects
print('\n## 8.1 Concatenating objects\n')

# 8.1.1 concat() function
# combine the measurements of NO2 and PM2.5 two tables with a similar structure, in a single table

# By default, concatenation is along axis 0, so the resulting table combines the rows of the input tables.
air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)

air_quality_axis_1 = pd.concat([air_quality_pm25, air_quality_no2], axis=1)
print('\nair_quality_axis_1:\n', air_quality_axis_1)

air_quality_head = air_quality.head()
print('air_quality_head:\n', air_quality_head)

print('Shape of the ``air_quality_pm25`` table: ', air_quality_pm25.shape)
print('Shape of the ``air_quality_no2`` table: ', air_quality_no2.shape)
print('Shape of the resulting ``air_quality`` table: ', air_quality.shape)

# 8.1.1.1 concat() function, axis = 0 and axis = 1
print("\n## 8.1.1.1 concat() function, axis = 0 and axis =1")
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

result_axis_0 = pd.concat([df1, df2], axis=0)
print('\nresult_axis_0:\n', result_axis_0)

result_axis_1 = pd.concat([df1, df2], axis=1)
print('\nresult_axis_1:\n', result_axis_1)

# 8.1.1.2 concat() function, mismatched columns (for axis=0) and mismatched indexes (for axis=1)
print("\n## 8.1.1.2 concat() function, mismatched columns (for axis=0) and mismatched indexes (for axis=1)\n")
# Mismatched Columns (for axis=0)
# join='outer' (default): Missing columns are filled with NaN.
# join='inner': Only common columns are kept.
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'C': [7, 8]})  # Column 'C' is new

# Default: outer join (keeps all columns, fills missing values with NaN)
result_outer = pd.concat([df1, df2], axis=0)
print("Outer join (axis=0):\n", result_outer)

# Inner join (only keeps common columns)
result_inner = pd.concat([df1, df2], axis=0, join='inner')
print("\nInner join (axis=0):\n", result_inner)

# Mismatched Indexes (for axis=1)
# join='outer' (default): Missing rows are filled with NaN.
# join='inner': Only common rows are kept.
df3 = pd.DataFrame({'A': [1, 2]}, index=[0, 1])
df4 = pd.DataFrame({'B': [3, 4]}, index=[1, 2])  # Index '2' is new

# Default: outer join (keeps all rows, fills missing values with NaN)
result_outer = pd.concat([df3, df4], axis=1)
print("Outer join (axis=1):\n", result_outer)

# Inner join (only keeps common rows)
result_inner = pd.concat([df3, df4], axis=1, join='inner')
print("\nInner join (axis=1):\n", result_inner)

# 8.1.1.3 concat() function with 'keys' argument
print("\n## 8.1.1.3 concat() function with 'keys' argument")
air_quality_with_keys = pd.concat([air_quality_pm25, air_quality_no2], keys=["PM25", "NO2"])
print("\nair_quality_with_keys:\n", air_quality_with_keys)

# 8.1.2 multi-indexing
# advanced indexing

# 8.1.3 reset_index

# 8.1.4 object concatenation
