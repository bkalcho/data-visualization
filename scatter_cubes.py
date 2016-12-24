# Author: Bojan G. Kalicanin
# Date: 24-Dec-2016
#
# 15-1. Cubes: A number raised to the third power is a cube. Plot the
# first five cubic numbers, and then plot the first 5000 cubic numbers.
#
# 15-2. Colored Cubes: Apply a colormap to your cubes plot.

import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
    edgecolors='none', s=20)

# Set chart title and label axis.
plt.title("Number Cubes", fontsize=24)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Cube of Values", fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

# Set axis limits.
plt.axis([0, 5100, 0, 132651000000])

plt.show()