# Author: Bojan G. Kalicanin
# Date: 24-Dec-2016
# 15-10. Practicing with Both Libraries: Try using matplotlib to make a
# die-rolling visualization, and use Pygal to make the visualization for
# a random walk.

import matplotlib.pyplot as plt
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and store results in a list.
results = []
[results.append(die_1.roll() + die_2.roll()) for roll_num in range(1000)]

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
[frequencies.append(results.count(value)) for value in range(2, max_result+1)]

x_values = [i for i in range(2, max_result+1)]

plt.scatter(x_values, frequencies, edgecolor='none', s=10)
plt.title("Rolling two dice results.", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Result", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.axis([1, max_result+1, 0, 1000/5])

plt.show()