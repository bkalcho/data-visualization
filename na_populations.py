# Author: Bojan G. Kalicanin
# Date: 27-Dec-2016
# Plot population of the three countries in North America.

import pygal.maps.world as worldmap

wm = worldmap.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
wm.render_to_file('na_populations.svg')