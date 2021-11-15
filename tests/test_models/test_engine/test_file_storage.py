#!/usr/bin/python3
"""
Test suite for file_storage engine
"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_private_attr(self):
        base = BaseModel()
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            file_path = storage.file_pate
        with self.assertRaises(AttributeError):
            file_path = storage.__file_pate

    def test_all(self):
        base = BaseModel()
        storage = FileStorage()
        self.assertEqual(base.__class__, BaseModel)
        self.assertEqual(storage.reload(), None)
        # base.save()
