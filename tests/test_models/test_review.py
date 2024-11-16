#!/usr/bin/env python3
"""Module for testing review class"""

import unittest
from models.review import Review


class test_Review(unittest.TestCase):
    """testing review class"""

    def test_review_attributes(self):
        """testing the attributes"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
