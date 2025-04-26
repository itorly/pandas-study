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

# In pandas we call these datetime objects similar to datetime.datetime from the standard library as pandas.Timestamp.

# 9.1.2 the use of pandas.Timestamp
print("\n## 9.1.2 the use of pandas.Timestamp")

# 9.1.2.1 min, max and difference
datetime_min = air_quality["datetime"].min()
print('\ndatetime_min:\n', datetime_min)

datetime_max = air_quality["datetime"].max()
print('\ndatetime_max:\n', datetime_max)

difference = datetime_max - datetime_min
# The result is a pandas.Timedelta object, similar to datetime.timedelta from the standard Python library and
# defining a time duration.
print('\ndifference:\n', difference)

# The various time concepts supported by pandas are explained in the user guide section on time related concepts.
# https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-overview

# 9.1.2.2 add a new column to the DataFrame containing only the month of the measurement
print("\n## 9.1.2.2 add a new column to the DataFrame containing only the month of the measurement")
air_quality["month"] = air_quality["datetime"].dt.month
air_quality_head_after_add_month = air_quality.head()
print('\nair_quality_head_after_add_month:\n', air_quality_head_after_add_month)

# 9.1.2.3 the average NO2 concentration for each day of the week for each of the measurement locations
print("\n## 9.1.2.3 the average NO2 concentration for each day of the week for each of the measurement locations")
# split-apply-combine
mean = air_quality.groupby(
    [air_quality["datetime"].dt.weekday, "location"])["value"].mean()

print('\nmean:\n', mean)

# 9.1.2.4 Plot the typical NO2 pattern during the day of our time series of all stations
print("\n## 9.1.2.4 Plot the typical NO2 pattern during the day of our time series of all stations")
# Create a figure and subplots with dimensions of 12x4 inches.
fig, axs = plt.subplots(figsize=(12, 4))
# split-apply-combine
plot = air_quality.groupby(air_quality["datetime"].dt.hour)["value"].mean().plot(kind='bar', rot=0, ax=axs)
print('\nplot:\n', plot)
# custom x label using Matplotlib
plt.xlabel("Hour of the day")

plt.ylabel("$NO_2 (µg/m^3)$")
plt.title("Typical NO2 pattern during the day")
# plt.show()
plt.savefig("output/9.1.2.4.png")


# 9.2 Datetime as index
print("\n## 9.2 Datetime as index")

# 9.2.1 pivot() function set the datetime as index
no2 = air_quality.pivot(index="datetime", columns="location", values="value")
print('\nno2:\n', no2)


