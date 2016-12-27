# Author: Bojan G. Kalicanin
# Date: 27-Dec-2016
# Print country codes in COUNTRIES dictionary but not used by population
# data.

import json
from pygal.maps.world import COUNTRIES

# Load data into list.
filename = 'population_data.json'
with open(filename) as f_obj:
    pop_data = json.load(f_obj)

country_names = []
for pop_cc in pop_data:
    country_names.append(pop_cc['Country Name'])

with open('print_cc.txt', 'w') as f_obj:
    for cc, name in sorted(COUNTRIES.items()):
        if name not in country_names:
            f_obj.write(cc + ': ' + name + '\n')