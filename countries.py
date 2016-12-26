# Author: Bojan G. Kalicanin
# Date: 26-Dec-2016
# Extracting Pygam Country Codes and Country Names.

from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])