import matplotlib.pyplot as plt
import pandas as pd
# PyCharm-Specific Fix,
# File → Settings → Tools → Python Plots → Uncheck "Show plots in tool window"
air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.plot()
plt.title('Air Quality - NO₂ Concentrations')
plt.ylabel('NO₂ (µg/m³)')
plt.show()


