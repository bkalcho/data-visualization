# Author: Bojan G. Kalicanin
# Date: 26-Dec-2016
# 16-3. Rainfall: Choose any location you’re interested in, and make a
# visualization that plots its rainfall. Start by focusing on one
# month's data, and then once your code is working, run it for a full
# year's data.

import csv
from datetime import datetime
from matplotlib import pyplot as plt

with open('precipitation_chicago_sep-2016.csv') as f_obj:
    reader = csv.reader(f_obj)
    header_row = next(reader)

    dates, precipitations = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            precipitation = float(row[19])
        except ValueError:
            print(current_date, 'missing_data')
        else:
            precipitations.append(precipitation)
            dates.append(current_date)

fig = plt.figure(dpi=110, figsize=(10, 6))
plt.plot(dates, precipitations, c='blue')

plt.title('Percipitation for Chicago area', fontsize=24)
plt.xlabel('', fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Percipitation [mm]", fontsize=14)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()