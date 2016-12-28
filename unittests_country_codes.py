# Author: Bojan G. Kalicanin
# Date: 28-Dec-2016
# 16-8. Testing the country_codes Module: When we wrote the
# country_codes module, we used print statements to check whether the
# get_country_code() function worked. Write a proper test for this
# function using what you learned in Chapter 11.

import unittest
from country_codes import get_country_code

class CountryCodesTestCases(unittest.TestCase):
    """Tests for 'country_codes.py'"""
    def test_country_codes(self):
        """Do countries like 'Andorra' work?"""
        cc = get_country_code('Andorra')
        self.assertEqual(cc, 'ad')

unittest.main()