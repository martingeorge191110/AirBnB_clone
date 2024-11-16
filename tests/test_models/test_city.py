#!/usr/bin/env python3
"""Module for testing city class"""
import unittest
from models.city import City


class test_City(unittest.TestCase):
    """testing class city"""
    def test_city_attributes(self):
        """testting attributes values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
