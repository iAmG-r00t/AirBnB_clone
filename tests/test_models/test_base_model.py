#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the base_model
    """
    def test_str(self):
        """
        checks the string output of an instance
        """
        base = BaseModel()
        self.assertEqual(base.__str__(), f"[{type(base).__name__}] ({base.id}) {base.__dict__}")

    def test_to_dict(self):
        """
        checks the to_dict() function of an instance
        """
        base = BaseModel()
        self.assertDictEqual(base.to_dict(), {'__class__': type(base).__name__, 'updated_at': base.updated_at.isoformat(), 'id': base.id, 'created_at': base.created_at.isoformat()})

    def test_attr_classes(self):
        """
        checks if the right classes were use to generate attributes
        """
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
