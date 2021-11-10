#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_str(self):
        base1 = BaseModel()
        id1 = base1.id
        dict1 = base1.__dict__
        self.assertEqual(base1.__class__, BaseModel)
        self.assertRegex(print(base1), \w+)

