#!/usr/bin/python3
"""Module for testing amenity class"""

import unittest
from models.amenity import Amenity


class test_Amenity(unittest.TestCase):
    """testing amenity class"""
    def test_amenity_attributes(self):
        """testing values"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
