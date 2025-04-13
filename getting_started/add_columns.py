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

# 5.2 rename columns
print('\n## 5.2 rename columns\n')
# 5.2.1 rename columns with fixed names
# rename the data columns to the corresponding station identifiers
air_quality_renamed = air_quality.rename(
    columns={
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
renamed_head = air_quality_renamed.head()
print('renamed_head:\n', renamed_head)

# 5.2.2 rename columns with a function
print('\n## 5.2.2 rename columns with a function\n')
# rename the data columns by replacing all spaces with underscores
air_quality_renamed = air_quality.rename(columns=lambda x: x.replace("_", " "))
renamed_head = air_quality_renamed.head()
print('renamed_head:\n', renamed_head)
