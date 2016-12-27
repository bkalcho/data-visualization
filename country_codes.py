# Author: Bojan G. Kalicanin
# Date: 26-Dec-2016
# Function that extract country codes.
# Implemented alternative checking for some countries as a soultion to
# the exercise 16-5. For the rest principle is the same.

from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    if country_name == 'Yemen, Rep.':
        return 'ye'
    elif country_name == 'Venezuela, RB':
        return 've'
    elif country_name == 'Vietnam':
        return 'vn'
    elif country_name == 'Slovak Republic':
        return 'sk'
    elif country_name == 'Macedonia, FYR':
        return 'mk'
    elif country_name == 'Korea, Rep.':
        return 'kr'
    elif country_name == 'Korea, Dem. Rep.':
        return 'kr'

    # If the country was't found, return None.
    return None

#print(get_country_code('Andorra'))
#print(get_country_code('United Arab Emirates'))
#print(get_country_code('Afghanistan'))