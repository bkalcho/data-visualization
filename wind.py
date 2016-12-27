# Author: Bojan G. Kalicanin
# Date: 26-Dec-2016
# 16-4. Explore: Generate a few more visualizations that examine any
# other weather aspect you’re interested in for any locations you’re
# curious about.

import csv
from datetime import datetime
from matplotlib import pyplot as plt

with open('moscow_nov_2015-2016.csv') as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)

    dates, wind_maxs, wind_means = [], [], []
    for row in reader:
        try:
            wind_max = int(row[16])
            wind_avg = int(row[17])
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
        except ValueError:
            print(current_date, 'missing_data')
        else:
            wind_maxs.append(wind_max)
            dates.append(current_date)
            wind_means.append(wind_avg)

fig = plt.figure(dpi=110, figsize=(10, 6))
plt.plot(dates, wind_maxs, c='red', alpha=0.5)
plt.plot(dates, wind_means, c='blue', alpha=0.5)
plt.fill_between(dates,wind_maxs, wind_means, facecolor='blue', alpha=0.1)
fig.autofmt_xdate()

plt.title("Daily high and avg wind speed", fontsize=24)
plt.xlabel('', fontsize=14)
plt.ylabel("Speed [km/h]", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()