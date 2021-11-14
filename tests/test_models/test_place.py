#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestBaseModel(unittest.TestCase):
    def test_str(self):
        place = Place()
        self.assertEqual(place.__class__, Place)

    def test_parent(self):
        place = Place()
        self.assertTrue(isinstance(place, BaseModel))
