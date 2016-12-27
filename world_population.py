# Author: Bojan G. Kalicanin
# Date: 26-Dec-2016
# World population visualisation for year 2010.

import json

import pygal.maps.world as pmw
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS

from country_codes import get_country_code

# Load data into list.
filename = 'population_data.json'
with open(filename) as f_obj:
    pop_data = json.load(f_obj)

# Build a dictionary of population data.
cc_populations = {}
# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            print('ERROR - ' + country_name)

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many functions are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RS('#336699', base_style=LCS)
wm = pmw.World(style=wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1b', cc_pops_2)
wm.add('>1b', cc_pops_3)

wm.render_to_file('world_population.svg')