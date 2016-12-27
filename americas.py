# Author: Bojan G. Kalicanin
# Date: 27-Dec-2016
# Map that highlights North America, Central America, and South America.

import pygal.maps.world as worldmap

wm = worldmap.World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe',
    'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')