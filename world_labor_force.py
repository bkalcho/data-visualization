# Author: Bojan G. Kalicanin
# Date: 27-Dec-2016
# World Labor Force analysis.

import csv
from country_codes import get_country_code
from pygal.maps.world import World
from pygal.style import RotateStyle, LightColorizedStyle

with open('labor_force.csv', 'r') as f_obj:
    reader = csv.reader(f_obj)
    for i in range(5):
        header_row = next(reader)

    lf_data = {}
    for row in reader:
        try:
            country_name = row[0]
            #country_code = row[1]
            lf_value = int(row[54])
        except ValueError:
            print(country_name + ': missing_data')
        else:
            lf_data[country_name] = lf_value

cc_lf = {}
for country, value in lf_data.items():
    code = get_country_code(country)
    if code:
        cc_lf[code] = value
    else:
        print('ERROR - ' + country_name)

cc_lf_1, cc_lf_2, cc_lf_3 = {}, {}, {}
for key, value in cc_lf.items():
    if value < 5000000:
        cc_lf_1[key] = value
    elif value < 50000000:
        cc_lf_2[key] = value
    else:
        cc_lf_3[key] = value

print(len(cc_lf_1), len(cc_lf_2), len(cc_lf_3))

wm_style = RotateStyle('#556677', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'Labor force by Country (year: 2010)'
wm.add('0-5m', cc_lf_1)
wm.add('5m-50m', cc_lf_2)
wm.add('>50m', cc_lf_3)

wm.render_to_file('world_labor_force.svg')