#!/usr/bin/env python3
"""Module for testing state class"""
import unittest
from models.state import State


class test_State(unittest.TestCase):
    """testing state class"""

    def test_state_attributes(self):
        """testing values"""
        state = State()
        self.assertEqual(state.name, "")
