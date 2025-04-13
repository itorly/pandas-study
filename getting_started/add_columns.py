# 5 add columns
print('# 5 add columns\n')
# How to create new columns derived from existing columns
import pandas as pd

air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

head = air_quality.head()
print('head:\n', head)

# 5.1 create a new column
print('\n## 5.1 create a new column\n')
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
head = air_quality.head()
print('head:\n', head)

air_quality["ratio"] = air_quality["station_paris"] / air_quality["station_london"]
head = air_quality.head()
print('head:\n', head)
