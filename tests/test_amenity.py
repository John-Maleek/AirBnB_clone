#!/usr/bin/python3
"""Test Amenity"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class Testamenity(unittest.TestCase):
    """
    unit test for amenity class
    """

    def test_class(self):
        """
        Tests if the class is named correctly.
        """
        amenity1 = Amenity()
        self.assertEqual(amenity1.__class__.__name__, "Amenity")

    def test_father(self):
        """
        Tests if class inherits from BaseModel.
        """
        amenity1 = Amenity()
        self.assertTrue(issubclass(amenity1.__class__, BaseModel))