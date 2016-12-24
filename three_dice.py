# Author: Bojan G. Kalicanin
# Date: 24-Dec-2016
# 15-8. Three Dice: If you roll three D6 dice, the smallest number you
# can roll is 3 and the largest number is 18. Create a visualization
# that shows what happens when you roll three D6 dice.

import pygal
from die import Die

# Create three D6 dice.
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Roll the dice 1000 times.
results = list()
[results.append(die_1.roll() + die_2.roll() + die_3.roll())
    for num_roll in range(1000)]

# Analyze the results.
frequencies = list()
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
[frequencies.append(results.count(value)) for value in range(3, max_result+1)]

# Create visualization for the rolls.
hist = pygal.Bar()
hist.title = "Results of rolling three D6 dice for 1,000 times."
hist.x_labels = [str(i) for i in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add("D6 + D6 + D6", frequencies)
hist.render_to_file("three_dice_visual.svg")