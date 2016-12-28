# Author: Bojan G. Kalicanin
# Date: 28-Dec-2016
#
# 17-3. Testing python_repos.py: In python_repos.py, we printed the 
# value of status_code to make sure the API call was successful. Write a
# program called test_python_repos.py, which uses unittest to assert
# that the value of status_code is 200. Figure out some other assertions
# you can make—for example, that the number of items returned is
# expected and that the total number of repositories is greater than a
# certain amount.

import unittest

import python_repos

class TestStatusCode(unittest.TestCase):
    """Unit test for testing Status Code of API call."""

    def test_status_code(self):
        """Is status code 200 returned?"""
        self.assertEqual(python_repos.r.status_code, 200)

unittest.main()