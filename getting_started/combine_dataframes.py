# 8 combine_dataframes
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