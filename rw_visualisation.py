# Author: Bojan G. Kalicanin
# Date: 24-Dec-2016
# 15-10. Practicing with Both Libraries: Try using matplotlib to make a
# die-rolling visualization, and use Pygal to make the visualization for
# a random walk.

import pygal
from random_walk import RandomWalk

# Make a random walk, and visualise.
rw = RandomWalk(1000)
rw.fill_walk()

hist = pygal.Bar()
hist.title = "Random Walk Visualisation"
hist.x_labels = list(rw.x_values)
hist.x_title = "X Values"
hist.y_title = "Y Values"
hist.add("RW", rw.y_values)
hist.render_to_file("rw_visualisation.svg")