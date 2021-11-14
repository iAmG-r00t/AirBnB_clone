#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestBaseModel(unittest.TestCase):
    def test_str(self):
        city = City()
        self.assertEqual(city.__class__, City)

    def test_parent(self):
        city = City()
        self.assertTrue(isinstance(city, BaseModel))
