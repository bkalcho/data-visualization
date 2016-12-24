# Author: Bojan G. Kalicanin
# Date: 24-Dec-2016
# 15-9. Multiplication: When you roll two dice, you usually add the two
# numbers together to get the result. Create a visualization that shows
# what happens if you multiply these numbers instead.

import pygal
from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Roll the dice 1000 times.
results = list()
[results.append(die_1.roll() * die_2.roll())
    for num_roll in range(1000)]

# Analyze the results.
frequencies = list()
max_result = die_1.num_sides * die_2.num_sides
[frequencies.append(results.count(value)) for value in range(1, max_result+1)]

# Create visualization for the rolls.
hist = pygal.Bar()
hist.title = "Results of rolling two D6 dice for 1,000 times."
hist.x_labels = [str(i) for i in range(1, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 * D6", frequencies)
hist.render_to_file("multiplication_visual.svg")