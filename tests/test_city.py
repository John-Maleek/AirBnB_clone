#!/usr/bin/python3
"""Test City"""

from models.base_model import BaseModel
from models.city import City
import unittest


class Testcity(unittest.TestCase):
    """
    Unittests for the City class.
    """

    def test_class(self):
        """
        Tests if class is named correctly.
        """
        city1 = City()
        self.assertEqual(city1.__class__.__name__, "City")

    def test_father(self):
        """
        Tests if Class inherits from BaseModel.
        """
        city1 = City()
        self.assertTrue(issubclass(city1.__class__, BaseModel))
