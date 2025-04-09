import matplotlib.pyplot as plt
import pandas as pd
# PyCharm-Specific Fix,
# File → Settings → Tools → Python Plots → Uncheck "Show plots in tool window"

# 4 plotting
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)

# 4.1 a quick visual check of the data
air_quality.plot()
plt.title('Air Quality - NO₂ Concentrations')
plt.ylabel('NO₂ (µg/m³)')
plt.show()

# 4.2 plot only the columns of the data table
air_quality["station_paris"].plot()
plt.title('Air Quality in Paris - NO₂ Concentrations')
plt.ylabel('NO₂ (µg/m³)')
plt.show()

# 4.3 scatter plot
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
plt.title('Air Quality measured in London versus Paris - NO₂ Concentrations')
plt.show()

# 4.4 method names of DataFrame.plot
method_names = [method_name for method_name in dir(air_quality.plot) if not method_name.startswith("_")]
print('method_names:\n', method_names)


