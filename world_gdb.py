# Author: Bojan G. Kalicanin
# Date: 27-Dec-2016
# Gross Domestic Product (GDP) for world countries.

import json

from country_codes import get_country_code

from pygal.maps.world import World

from pygal.style import RotateStyle, LightColorizedStyle

filename = 'gdb.json'
cc_gdb = {}
with open(filename, 'r') as f_obj:
    gdb_data = json.load(f_obj)

    for gdb_dict in gdb_data:
        if gdb_dict['Year'] == '2014':
            country_name = gdb_dict['Country Name']
            gdb_value = float(gdb_dict['Value'])
            code = get_country_code(country_name)
            if code:
                cc_gdb[code] = gdb_value
            else:
                print('ERROR - ' + country_name)

cc_gdb_1, cc_gdb_2, cc_gdb_3, cc_gdb_4 = {}, {}, {}, {}
for cc, gdb in cc_gdb.items():
    if gdb < 10000000000:
        cc_gdb_1[cc] = gdb
    elif gdb < 100000000000:
        cc_gdb_2[cc] = gdb
    elif gdb < 1000000000000:
        cc_gdb_3[cc] = gdb
    else:
        cc_gdb_4[cc] = gdb

print(len(cc_gdb_1), len(cc_gdb_2), len(cc_gdb_3), len(cc_gdb_4))

wm_style = RotateStyle('#663399', base_style=LightColorizedStyle)
wm = World(style=wm_style)
wm.title = 'GDB in USD($) for world countries for year 2014'
wm.add('GDB: 0-10b', cc_gdb_1)
wm.add('GDB: 10b-100b', cc_gdb_2)
wm.add('GDB: 100b-1000b', cc_gdb_3)
wm.add('GDB: >1000b', cc_gdb_4)

wm.render_to_file('world_gdb.svg')