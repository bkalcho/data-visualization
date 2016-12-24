# Author: Bojan G. Kalicanin
# Date: 24-Dec-2016
# Visual representation of rolling dice.

import pygal
from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = []
[results.append(die.roll()) for roll_num in range(1000)]

# Analyze the results.
frequencies = []
[frequencies.append(results.count(value))
    for value in range(1, die.num_sides+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [str(i) for i in range(1, die.num_sides+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
#print(frequencies)