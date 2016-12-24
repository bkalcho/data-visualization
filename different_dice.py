# Author: Bojan G. Kalicanin
# Date: 24-Dec-2016
# Visual representation of rolling two different dice.

import pygal
from die import Die

# Create a D6 and a D10 dice.
die_1 = Die()
die_2 = Die(10)


# Make some rolls, and store results in a list.
results = []
[results.append(die_1.roll() + die_2.roll()) for roll_num in range(50000)]

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
[frequencies.append(results.count(value)) for value in range(2, max_result+1)]

# Visualize the results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and D10 dice 50,000 times."
hist.x_labels = [str(i) for i in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('diff_dice_visual.svg')