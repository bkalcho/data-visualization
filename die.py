# Author: Bojan G. Kalicanin
# Date: 24-Dec-2016
# Modelling a dice.

from random import randint

class Die(object):
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)