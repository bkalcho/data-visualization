# Author: Bojan G. Kalicanin
# Date: 26-Dec-2016
# World population visualisation for year 2010.

import json

# Load data into list.
filename = 'population_data.json'
with open(filename) as f_obj:
    pop_data = json.load(f_obj)

# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ": " + population)