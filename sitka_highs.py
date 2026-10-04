from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

# path = Path("weather_data/sitka_weather_07-2021_simple.csv")
path1 = Path("weather_data/sitka_weather_2021_simple.csv")
lines = path1.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# Extraact dates and high and low temperatures
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(current_date)
    low = int(row[5])
    lows.append(low)
    high = int(row[4])
    highs.append(high)

# plot the high temprature
plt.style.use("seaborn-v0_8")
fig, ax = plt.subplots()
ax.plot(dates, highs, color="red", alpha=0.5)
ax.plot(dates, lows, color="blue", alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

# format plot
ax.set_title("Dayliy high and low tempratures, 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temprature (F)", fontsize=16)
ax.tick_params(labelsize=16)
plt.show()
