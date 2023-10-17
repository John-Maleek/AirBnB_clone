#!/usr/bin/python3
"""Test Review"""

from models.base_model import BaseModel
from models.review import Review
import unittest


class Testreview(unittest.TestCase):
    """
    Unittests for the Review class.
    """

    def test_class(self):
        """
        Tests if class is named correctly.
        """
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_father(self):
        """
        Tests if Class inherits from BaseModel.
        """
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))
