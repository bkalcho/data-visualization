# Author: Bojan G. Kalicanin
# Date: 26-Dec-2016
# Function that extract country codes.

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country was't found, return None.
    return None

#print(get_country_code('Andorra'))
#print(get_country_code('United Arab Emirates'))
#print(get_country_code('Afghanistan'))