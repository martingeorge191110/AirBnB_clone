#!/usr/bin/python3

"""module for unittesting of Basemodel class methods"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class BasemodelTest(unittest.TestCase):
    """Test cases for BaseModel Class"""

    def setUp(self):
        """Initializes for the tests."""
        self.test = BaseModel()
        self.dict = self.test.to_dict()
        self.test_kwargs_init = BaseModel(id="123123")

    def test_instance_creation(self):
        """Testing if BaseModel is created correctly."""
        self.assertIsInstance(self.test, BaseModel)
        self.assertIsInstance(self.test.created_at, datetime)
        self.assertIsInstance(self.test.updated_at, datetime)

    def test_save(self):
        """Testting save method"""
        old_updated_at = self.test.updated_at
        self.test.save()
        self.assertNotEqual(old_updated_at, self.test.updated_at)

    def test_to_dict(self):
        """Testting to_dict method"""
        out_dict = {
            "__class__": "BaseModel",
            "id": self.test.id,
            "created_at": self.test.created_at.isoformat(),
            "updated_at": self.test.updated_at.isoformat(),
        }
        self.assertEqual(self.dict, out_dict)

    def test_kwargs(self):
        out_put = "[BaseModel] (123123) {'id': '123123'}"
        self.assertEqual(self.test_kwargs_init.__str__(), out_put)


if __name__ == '__main__':
    unittest.main()
