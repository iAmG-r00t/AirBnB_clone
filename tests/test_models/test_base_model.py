#!/usr/bin/python3
"""
Test suite for base_model
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_str(self):
        base = BaseModel()
        self.assertEqual(base.__str__(), f"[{type(base).__name__}] ({base.id}) {base.__dict__}")
